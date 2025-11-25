// API Client for backend communication
class API {
    constructor() {
        this.baseURL = API_CONFIG.baseURL;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;

        try {
            const response = await fetch(url, {
                ...options,
                headers: {
                    ...options.headers
                }
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Request failed');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    // Get all documents with filters
    async getDocuments(filters = {}) {
        const params = new URLSearchParams();

        if (filters.category) params.append('category', filters.category);
        if (filters.file_type) params.append('file_type', filters.file_type);
        if (filters.search) params.append('search', filters.search);
        if (filters.limit) params.append('limit', filters.limit);
        if (filters.offset) params.append('offset', filters.offset);

        const query = params.toString();
        const endpoint = query ? `${API_CONFIG.endpoints.documents}?${query}` : API_CONFIG.endpoints.documents;

        return await this.request(endpoint);
    }

    // Get single document
    async getDocument(id) {
        return await this.request(`${API_CONFIG.endpoints.documents}/${id}`);
    }

    // Upload file
    async uploadFile(file, useAI = false) {
        const formData = new FormData();
        formData.append('file', file);

        const endpoint = useAI ? API_CONFIG.endpoints.uploadAnalyze : API_CONFIG.endpoints.upload;

        return await this.request(endpoint, {
            method: 'POST',
            body: formData
        });
    }

    // Update document
    async updateDocument(id, data) {
        return await this.request(`${API_CONFIG.endpoints.documents}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
    }

    // Delete document
    async deleteDocument(id) {
        return await this.request(`${API_CONFIG.endpoints.documents}/${id}`, {
            method: 'DELETE'
        });
    }

    // Analyze document with AI
    async analyzeDocument(id) {
        return await this.request(`${API_CONFIG.endpoints.documents}/${id}/analyze`, {
            method: 'POST'
        });
    }

    // Get analytics
    async getAnalytics() {
        return await this.request(API_CONFIG.endpoints.analytics);
    }
}

// Global API instance
const api = new API();
