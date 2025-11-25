# n8n Workflows - Guia de Uso

Este diretório contém workflows n8n prontos para automatizar processos no Sistema de Gestão de Documentos.

## 📋 Workflows Disponíveis

### 1. Document Processing (`document-processing.json`)
**Objetivo**: Processar automaticamente documentos após upload

**Fluxo**:
1. Recebe webhook quando documento é enviado
2. Analisa documento com OpenAI
3. Atualiza metadados automaticamente
4. Retorna confirmação

**Como usar**:
- Importe o workflow no n8n
- Configure o webhook URL
- Integre com o backend para chamar o webhook após upload

---

### 2. Daily Notifications (`notifications.json`)
**Objetivo**: Enviar resumo diário de documentos por email

**Fluxo**:
1. Executa diariamente às 9h
2. Busca estatísticas da API
3. Envia email com resumo

**Como usar**:
- Importe o workflow no n8n
- Configure credenciais de email (SMTP)
- Ajuste destinatários e horário conforme necessário

---

### 3. Weekly Backup (`backup-export.json`)
**Objetivo**: Backup semanal automático para cloud storage

**Fluxo**:
1. Executa semanalmente (domingo 2h)
2. Exporta todos os documentos
3. Converte para JSON
4. Salva no Google Drive

**Como usar**:
- Importe o workflow no n8n
- Configure credenciais do Google Drive
- Ajuste frequência se necessário

---

## 🚀 Como Importar Workflows

1. Abra o n8n (local ou cloud)
2. Clique em **Workflows** > **Import from File**
3. Selecione o arquivo JSON do workflow
4. Configure as credenciais necessárias
5. Ative o workflow

## ⚙️ Configurações Necessárias

### Credenciais
- **Email/SMTP**: Para notificações
- **Google Drive**: Para backups (ou outro storage)
- **Webhook URLs**: Configure no backend

### Variáveis de Ambiente
```bash
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your-password
```

## 🔧 Customização

Você pode modificar os workflows para:
- Adicionar Slack/Discord notifications
- Integrar com outras ferramentas (Notion, Airtable)
- Criar workflows personalizados para seu processo
- Adicionar validações e regras de negócio

## 📚 Recursos

- [Documentação n8n](https://docs.n8n.io/)
- [Community Workflows](https://n8n.io/workflows)
- [n8n Forum](https://community.n8n.io/)
