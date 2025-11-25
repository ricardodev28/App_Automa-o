-- =====================================================
-- Document Management System - Supabase Schema
-- =====================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =====================================================
-- Categories Table
-- =====================================================
CREATE TABLE IF NOT EXISTS categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    color VARCHAR(7) DEFAULT '#6366f1',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Insert default categories
INSERT INTO categories (name, description, color) VALUES
    ('Financeiro', 'Documentos financeiros e contábeis', '#10b981'),
    ('RH', 'Recursos Humanos e gestão de pessoas', '#f59e0b'),
    ('Técnico', 'Documentação técnica e especificações', '#3b82f6'),
    ('Marketing', 'Materiais de marketing e comunicação', '#ec4899'),
    ('Legal', 'Documentos jurídicos e contratos', '#8b5cf6'),
    ('Geral', 'Documentos gerais', '#6b7280')
ON CONFLICT (name) DO NOTHING;

-- =====================================================
-- Documents Table
-- =====================================================
CREATE TABLE IF NOT EXISTS documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100),
    category VARCHAR(50) DEFAULT 'Geral',
    tags TEXT[] DEFAULT '{}',
    description TEXT,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size BIGINT NOT NULL,
    file_url TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Foreign key to categories
    CONSTRAINT fk_category FOREIGN KEY (category) 
        REFERENCES categories(name) 
        ON UPDATE CASCADE 
        ON DELETE SET DEFAULT
);

-- =====================================================
-- Indexes for Performance
-- =====================================================

-- Index for category filtering
CREATE INDEX IF NOT EXISTS idx_documents_category ON documents(category);

-- Index for file type filtering
CREATE INDEX IF NOT EXISTS idx_documents_file_type ON documents(file_type);

-- Index for created_at sorting
CREATE INDEX IF NOT EXISTS idx_documents_created_at ON documents(created_at DESC);

-- Index for text search on title
CREATE INDEX IF NOT EXISTS idx_documents_title ON documents USING gin(to_tsvector('portuguese', title));

-- Index for text search on author
CREATE INDEX IF NOT EXISTS idx_documents_author ON documents USING gin(to_tsvector('portuguese', author));

-- Index for array search on tags
CREATE INDEX IF NOT EXISTS idx_documents_tags ON documents USING gin(tags);

-- =====================================================
-- Functions and Triggers
-- =====================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to automatically update updated_at
DROP TRIGGER IF EXISTS update_documents_updated_at ON documents;
CREATE TRIGGER update_documents_updated_at
    BEFORE UPDATE ON documents
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- =====================================================
-- Row Level Security (RLS)
-- =====================================================

-- Enable RLS on documents table
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Policy: Allow all operations for authenticated users
CREATE POLICY "Allow all for authenticated users" ON documents
    FOR ALL
    USING (true)
    WITH CHECK (true);

-- Policy: Allow read for anonymous users (optional - remove if you want auth only)
CREATE POLICY "Allow read for anonymous" ON documents
    FOR SELECT
    USING (true);

-- Enable RLS on categories table
ALTER TABLE categories ENABLE ROW LEVEL SECURITY;

-- Policy: Allow read for all users
CREATE POLICY "Allow read for all" ON categories
    FOR SELECT
    USING (true);

-- =====================================================
-- Storage Bucket
-- =====================================================

-- Create storage bucket for documents
-- Note: This needs to be done via Supabase Dashboard or API
-- Run this in the Supabase SQL Editor:

-- INSERT INTO storage.buckets (id, name, public)
-- VALUES ('documents', 'documents', true)
-- ON CONFLICT (id) DO NOTHING;

-- =====================================================
-- Useful Views
-- =====================================================

-- View: Document statistics by category
CREATE OR REPLACE VIEW document_stats_by_category AS
SELECT 
    c.name AS category,
    c.color,
    COUNT(d.id) AS document_count,
    COALESCE(SUM(d.file_size), 0) AS total_size,
    ROUND(COUNT(d.id)::NUMERIC / NULLIF((SELECT COUNT(*) FROM documents), 0) * 100, 2) AS percentage
FROM categories c
LEFT JOIN documents d ON d.category = c.name
GROUP BY c.name, c.color
ORDER BY document_count DESC;

-- View: Recent documents
CREATE OR REPLACE VIEW recent_documents AS
SELECT 
    id,
    title,
    author,
    category,
    tags,
    file_type,
    created_at
FROM documents
ORDER BY created_at DESC
LIMIT 10;

-- =====================================================
-- Sample Queries
-- =====================================================

-- Get all documents with category info
-- SELECT d.*, c.color 
-- FROM documents d 
-- JOIN categories c ON d.category = c.name;

-- Search documents by text
-- SELECT * FROM documents 
-- WHERE to_tsvector('portuguese', title || ' ' || COALESCE(description, '')) 
-- @@ to_tsquery('portuguese', 'search_term');

-- Get documents by tag
-- SELECT * FROM documents WHERE 'tag_name' = ANY(tags);

-- Get document count by file type
-- SELECT file_type, COUNT(*) as count 
-- FROM documents 
-- GROUP BY file_type 
-- ORDER BY count DESC;
