// Dashboard and Analytics
class Dashboard {
    constructor() {
        this.categoryChart = null;
        this.tagsChart = null;
    }

    async init() {
        await this.loadAnalytics();
    }

    async loadAnalytics() {
        try {
            const data = await api.getAnalytics();
            this.updateStats(data);
            this.updateCharts(data);
        } catch (error) {
            console.error('Error loading analytics:', error);
            ui.showToast('Erro ao carregar analytics', 'error');
        }
    }

    updateStats(data) {
        // Update stat cards
        document.getElementById('totalDocs').textContent = data.total_documents || 0;
        document.getElementById('totalSize').textContent = ui.formatFileSize(data.total_size || 0);
        document.getElementById('totalTags').textContent = data.top_tags?.length || 0;

        // Categories count is fixed at 6
        document.getElementById('totalCategories').textContent = '6';
    }

    updateCharts(data) {
        this.createCategoryChart(data.categories || []);
        this.createTagsChart(data.top_tags || []);
    }

    createCategoryChart(categories) {
        const ctx = document.getElementById('categoryChart');
        if (!ctx) return;

        // Destroy existing chart
        if (this.categoryChart) {
            this.categoryChart.destroy();
        }

        const labels = categories.map(c => c.category);
        const values = categories.map(c => c.count);
        const colors = categories.map(c => CATEGORY_COLORS[c.category] || '#6b7280');

        this.categoryChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: values,
                    backgroundColor: colors,
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 15,
                            font: {
                                size: 12,
                                family: 'Inter'
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                const label = context.label || '';
                                const value = context.parsed || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: ${value} (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }

    createTagsChart(tags) {
        const ctx = document.getElementById('tagsChart');
        if (!ctx) return;

        // Destroy existing chart
        if (this.tagsChart) {
            this.tagsChart.destroy();
        }

        // Take top 10 tags
        const topTags = tags.slice(0, 10);
        const labels = topTags.map(t => t.tag);
        const values = topTags.map(t => t.count);

        this.tagsChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Frequência',
                    data: values,
                    backgroundColor: 'rgba(99, 102, 241, 0.8)',
                    borderColor: 'rgba(99, 102, 241, 1)',
                    borderWidth: 2,
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1,
                            font: {
                                family: 'Inter'
                            }
                        },
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        }
                    },
                    x: {
                        ticks: {
                            font: {
                                family: 'Inter'
                            }
                        },
                        grid: {
                            display: false
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return `Usado ${context.parsed.y} vezes`;
                            }
                        }
                    }
                }
            }
        });
    }

    async refresh() {
        ui.showToast('Atualizando dashboard...', 'info');
        await this.loadAnalytics();
        await app.loadDocuments();
        ui.showToast('Dashboard atualizado!', 'success');
    }
}

// Global dashboard instance
const dashboard = new Dashboard();
