// API Configuration
const API_CONFIG = {
    baseURL: 'http://localhost:8000',
    endpoints: {
        documents: '/api/documents',
        analytics: '/api/analytics/stats',
        upload: '/api/documents/upload',
        uploadAnalyze: '/api/documents/analyze-upload'
    }
};

// Category colors mapping
const CATEGORY_COLORS = {
    'Financeiro': '#10b981',
    'RH': '#f59e0b',
    'Técnico': '#3b82f6',
    'Marketing': '#ec4899',
    'Legal': '#8b5cf6',
    'Geral': '#6b7280'
};

// File type icons
const FILE_ICONS = {
    'pdf': '📄',
    'docx': '📝',
    'doc': '📝',
    'txt': '📃',
    'xlsx': '📊',
    'xls': '📊',
    'pptx': '📽️',
    'ppt': '📽️',
    'jpg': '🖼️',
    'jpeg': '🖼️',
    'png': '🖼️',
    'gif': '🖼️',
    'default': '📁'
};
