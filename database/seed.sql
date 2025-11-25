-- =====================================================
-- Sample Data for Testing
-- =====================================================

-- Sample documents (you can customize these)
INSERT INTO documents (title, author, category, tags, description, file_name, file_type, file_size, file_url) VALUES
    (
        'Relatório Financeiro Q4 2024',
        'Maria Silva',
        'Financeiro',
        ARRAY['relatório', 'financeiro', 'q4', '2024'],
        'Relatório financeiro do quarto trimestre de 2024 com análise de receitas e despesas.',
        'relatorio_financeiro_q4_2024.pdf',
        'pdf',
        2048576,
        'https://example.com/sample.pdf'
    ),
    (
        'Manual de Onboarding',
        'João Santos',
        'RH',
        ARRAY['onboarding', 'rh', 'manual', 'treinamento'],
        'Manual completo para integração de novos colaboradores.',
        'manual_onboarding.docx',
        'docx',
        1024000,
        'https://example.com/sample.docx'
    ),
    (
        'Especificação Técnica - API v2',
        'Carlos Oliveira',
        'Técnico',
        ARRAY['api', 'especificação', 'técnico', 'v2'],
        'Documentação técnica da API versão 2.0 com endpoints e exemplos.',
        'api_spec_v2.pdf',
        'pdf',
        3145728,
        'https://example.com/sample.pdf'
    ),
    (
        'Campanha Marketing Digital 2025',
        'Ana Costa',
        'Marketing',
        ARRAY['marketing', 'digital', 'campanha', '2025'],
        'Planejamento da campanha de marketing digital para 2025.',
        'campanha_2025.pptx',
        'pptx',
        5242880,
        'https://example.com/sample.pptx'
    ),
    (
        'Contrato de Prestação de Serviços',
        'Dr. Pedro Alves',
        'Legal',
        ARRAY['contrato', 'legal', 'serviços'],
        'Modelo de contrato de prestação de serviços.',
        'contrato_servicos.pdf',
        'pdf',
        512000,
        'https://example.com/sample.pdf'
    ),
    (
        'Ata de Reunião - Janeiro 2025',
        'Equipe Gestão',
        'Geral',
        ARRAY['ata', 'reunião', 'janeiro'],
        'Ata da reunião mensal de janeiro de 2025.',
        'ata_janeiro_2025.docx',
        'docx',
        256000,
        'https://example.com/sample.docx'
    );

-- Note: The file_url values above are placeholders.
-- In production, these will be actual Supabase Storage URLs.
