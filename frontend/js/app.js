// Main Application Logic
class DocumentManager {
    constructor() {
        this.documents = [];
        this.currentDocument = null;
        this.currentAIAnalysis = null;
        this.filters = {
            category: '',
            file_type: '',
            search: ''
        };
    }

    async init() {
        this.setupEventListeners();
        await this.loadDocuments();
        await dashboard.init();
    }

    setupEventListeners() {
        // File input
        const fileInput = document.getElementById('fileInput');
        fileInput.addEventListener('change', (e) => this.handleFileSelect(e));

        // Drag and drop
        const uploadArea = document.getElementById('uploadArea');
        uploadArea.addEventListener('click', () => fileInput.click());
        uploadArea.addEventListener('dragover', (e) => this.handleDragOver(e));
        uploadArea.addEventListener('dragleave', (e) => this.handleDragLeave(e));
        uploadArea.addEventListener('drop', (e) => this.handleDrop(e));

        // Search and filters
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', (e) => this.handleSearch(e));

        const categoryFilter = document.getElementById('categoryFilter');
        categoryFilter.addEventListener('change', (e) => this.handleCategoryFilter(e));

        const typeFilter = document.getElementById('typeFilter');
        typeFilter.addEventListener('change', (e) => this.handleTypeFilter(e));
    }

    // File handling
    handleDragOver(e) {
        e.preventDefault();
        e.stopPropagation();
        e.currentTarget.classList.add('drag-over');
    }

    handleDragLeave(e) {
        e.preventDefault();
        e.stopPropagation();
        e.currentTarget.classList.remove('drag-over');
    }

    handleDrop(e) {
        e.preventDefault();
        e.stopPropagation();
        e.currentTarget.classList.remove('drag-over');

        const files = Array.from(e.dataTransfer.files);
        this.uploadFiles(files);
    }

    handleFileSelect(e) {
        const files = Array.from(e.target.files);
        this.uploadFiles(files);
        e.target.value = ''; // Reset input
    }

    async uploadFiles(files) {
        if (files.length === 0) return;

        const useAI = document.getElementById('aiAnalysisCheckbox').checked;
        ui.showLoading('uploadProgress');

        let successCount = 0;
        let errorCount = 0;

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const progress = ((i + 1) / files.length) * 100;
            ui.updateProgress(progress);

            try {
                await api.uploadFile(file, useAI);
                successCount++;
            } catch (error) {
                console.error(`Error uploading ${file.name}:`, error);
                errorCount++;
            }
        }

        ui.hideLoading('uploadProgress');

        if (successCount > 0) {
            ui.showToast(`${successCount} arquivo(s) enviado(s) com sucesso!`, 'success');
            await this.loadDocuments();
            await dashboard.loadAnalytics();
        }

        if (errorCount > 0) {
            ui.showToast(`${errorCount} arquivo(s) falharam no upload`, 'error');
        }
    }

    // Load and display documents
    async loadDocuments() {
        try {
            this.documents = await api.getDocuments(this.filters);
            this.renderDocuments();
        } catch (error) {
            console.error('Error loading documents:', error);
            ui.showToast('Erro ao carregar documentos', 'error');
        }
    }

    renderDocuments() {
        const grid = document.getElementById('documentsGrid');
        const emptyState = document.getElementById('emptyState');
        const countElement = document.getElementById('documentsCount');

        if (this.documents.length === 0) {
            grid.innerHTML = '';
            emptyState.classList.remove('hidden');
            countElement.textContent = '0 documentos encontrados';
            return;
        }

        emptyState.classList.add('hidden');
        countElement.textContent = `${this.documents.length} documento(s) encontrado(s)`;

        grid.innerHTML = this.documents.map(doc => this.createDocumentCard(doc)).join('');
    }

    createDocumentCard(doc) {
        const icon = ui.getFileIcon(doc.file_type);
        const tags = doc.tags?.map(tag => `<span class="tag">${tag}</span>`).join('') || '';
        const author = doc.author || 'Desconhecido';
        const date = ui.formatDate(doc.created_at);
        const size = ui.formatFileSize(doc.file_size);

        return `
            <div class="document-card">
                <div class="document-header">
                    <div class="document-icon">${icon}</div>
                    <div class="document-actions">
                        <button class="icon-btn" onclick="app.analyzeWithAI('${doc.id}')" title="Analisar com IA">
                            🤖
                        </button>
                        <button class="icon-btn" onclick="app.editDocument('${doc.id}')" title="Editar">
                            ✏️
                        </button>
                        <button class="icon-btn" onclick="app.deleteDocument('${doc.id}')" title="Excluir">
                            🗑️
                        </button>
                    </div>
                </div>
                <h3 class="document-title">${doc.title}</h3>
                <div class="document-meta">
                    <span>👤 ${author}</span>
                    <span>📅 ${date}</span>
                    <span>💾 ${size}</span>
                </div>
                <div class="document-tags">
                    ${tags}
                </div>
                <span class="category-badge category-${doc.category}">${doc.category}</span>
            </div>
        `;
    }

    // Edit document
    async editDocument(id) {
        try {
            const doc = await api.getDocument(id);
            this.currentDocument = doc;

            // Populate form
            document.getElementById('editTitle').value = doc.title;
            document.getElementById('editAuthor').value = doc.author || '';
            document.getElementById('editCategory').value = doc.category;
            document.getElementById('editTags').value = doc.tags?.join(', ') || '';
            document.getElementById('editDescription').value = doc.description || '';

            ui.openModal('editModal');
        } catch (error) {
            console.error('Error loading document:', error);
            ui.showToast('Erro ao carregar documento', 'error');
        }
    }

    async saveDocument() {
        if (!this.currentDocument) return;

        const title = document.getElementById('editTitle').value;
        const author = document.getElementById('editAuthor').value;
        const category = document.getElementById('editCategory').value;
        const tagsInput = document.getElementById('editTags').value;
        const description = document.getElementById('editDescription').value;

        const tags = tagsInput.split(',').map(t => t.trim()).filter(t => t);

        try {
            await api.updateDocument(this.currentDocument.id, {
                title,
                author: author || null,
                category,
                tags,
                description: description || null
            });

            ui.showToast('Documento atualizado com sucesso!', 'success');
            ui.closeModal('editModal');
            await this.loadDocuments();
            await dashboard.loadAnalytics();
        } catch (error) {
            console.error('Error updating document:', error);
            ui.showToast('Erro ao atualizar documento', 'error');
        }
    }

    // Delete document
    async deleteDocument(id) {
        if (!confirm('Tem certeza que deseja excluir este documento?')) {
            return;
        }

        try {
            await api.deleteDocument(id);
            ui.showToast('Documento excluído com sucesso!', 'success');
            await this.loadDocuments();
            await dashboard.loadAnalytics();
        } catch (error) {
            console.error('Error deleting document:', error);
            ui.showToast('Erro ao excluir documento', 'error');
        }
    }

    // AI Analysis
    async analyzeWithAI(id) {
        try {
            const doc = await api.getDocument(id);
            this.currentDocument = doc;

            ui.openModal('aiModal');
            document.getElementById('aiLoading').classList.remove('hidden');
            document.getElementById('aiResults').classList.add('hidden');
            document.getElementById('applyAiBtn').disabled = true;

            const analysis = await api.analyzeDocument(id);
            this.currentAIAnalysis = analysis;

            // Display results
            document.getElementById('aiTitle').textContent = analysis.suggested_title || 'N/A';
            document.getElementById('aiAuthor').textContent = analysis.suggested_author || 'N/A';
            document.getElementById('aiCategory').textContent = analysis.suggested_category || 'N/A';
            document.getElementById('aiSummary').textContent = analysis.summary || 'N/A';

            const tagsContainer = document.getElementById('aiTags');
            tagsContainer.innerHTML = analysis.suggested_tags?.map(tag =>
                `<span class="tag">${tag}</span>`
            ).join('') || 'Nenhuma tag sugerida';

            const confidence = Math.round(analysis.confidence * 100);
            document.getElementById('confidenceLevel').style.width = `${confidence}%`;
            document.getElementById('confidenceText').textContent = `${confidence}%`;

            document.getElementById('aiLoading').classList.add('hidden');
            document.getElementById('aiResults').classList.remove('hidden');
            document.getElementById('applyAiBtn').disabled = false;
        } catch (error) {
            console.error('Error analyzing document:', error);
            ui.showToast('Erro ao analisar documento com IA', 'error');
            ui.closeModal('aiModal');
        }
    }

    async applyAiSuggestions() {
        if (!this.currentDocument || !this.currentAIAnalysis) return;

        try {
            await api.updateDocument(this.currentDocument.id, {
                title: this.currentAIAnalysis.suggested_title,
                author: this.currentAIAnalysis.suggested_author,
                category: this.currentAIAnalysis.suggested_category,
                tags: this.currentAIAnalysis.suggested_tags,
                description: this.currentAIAnalysis.summary
            });

            ui.showToast('Sugestões da IA aplicadas com sucesso!', 'success');
            ui.closeModal('aiModal');
            await this.loadDocuments();
            await dashboard.loadAnalytics();
        } catch (error) {
            console.error('Error applying AI suggestions:', error);
            ui.showToast('Erro ao aplicar sugestões', 'error');
        }
    }

    // Filters
    handleSearch(e) {
        this.filters.search = e.target.value;
        this.debounceLoadDocuments();
    }

    handleCategoryFilter(e) {
        this.filters.category = e.target.value;
        this.loadDocuments();
    }

    handleTypeFilter(e) {
        this.filters.file_type = e.target.value;
        this.loadDocuments();
    }

    debounceLoadDocuments() {
        clearTimeout(this.debounceTimer);
        this.debounceTimer = setTimeout(() => {
            this.loadDocuments();
        }, 300);
    }
}

// Global app instance
const app = new DocumentManager();

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    app.init();
});
