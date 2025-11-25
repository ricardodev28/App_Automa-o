# 🔧 Setup Guide - Passo a Passo

Este guia detalha a configuração completa do projeto do zero.

---

## 📋 Índice

1. [Configurar Supabase](#1-configurar-supabase)
2. [Configurar OpenAI](#2-configurar-openai)
3. [Configurar Backend Python](#3-configurar-backend-python)
4. [Configurar Frontend](#4-configurar-frontend)
5. [Configurar n8n (Opcional)](#5-configurar-n8n-opcional)
6. [Verificação e Testes](#6-verificação-e-testes)

---

## 1. Configurar Supabase

### 1.1 Criar Projeto

1. Acesse [supabase.com](https://supabase.com)
2. Clique em "Start your project"
3. Crie uma conta (GitHub, Google, ou email)
4. Clique em "New Project"
5. Preencha:
   - **Name**: Document Management
   - **Database Password**: (crie uma senha forte)
   - **Region**: escolha a mais próxima
6. Aguarde a criação do projeto (~2 minutos)

### 1.2 Obter Credenciais

1. No dashboard do projeto, vá em **Settings** > **API**
2. Copie:
   - **Project URL** (ex: `https://xxxxx.supabase.co`)
   - **anon public** key (chave longa começando com `eyJ...`)

### 1.3 Executar Schema SQL

1. No menu lateral, clique em **SQL Editor**
2. Clique em **New Query**
3. Abra o arquivo `database/schema.sql` do projeto
4. Copie TODO o conteúdo
5. Cole no SQL Editor
6. Clique em **Run** (ou pressione Ctrl+Enter)
7. Aguarde a confirmação "Success. No rows returned"

### 1.4 (Opcional) Inserir Dados de Exemplo

1. No SQL Editor, crie uma nova query
2. Abra `database/seed.sql`
3. Copie e cole o conteúdo
4. Execute com **Run**

### 1.5 Criar Storage Bucket

1. No menu lateral, clique em **Storage**
2. Clique em **Create a new bucket**
3. Preencha:
   - **Name**: `documents`
   - **Public bucket**: ✅ Marque como público
4. Clique em **Create bucket**

### 1.6 Configurar Storage Policies

1. Clique no bucket `documents`
2. Vá em **Policies**
3. Clique em **New Policy**
4. Selecione template "Allow public access to bucket"
5. Confirme

✅ **Supabase configurado!**

---

## 2. Configurar OpenAI

### 2.1 Criar Conta

1. Acesse [platform.openai.com](https://platform.openai.com)
2. Crie uma conta ou faça login
3. Adicione método de pagamento em **Billing**
4. (Opcional) Configure limites de gasto em **Usage limits**

### 2.2 Criar API Key

1. Vá em **API Keys** no menu
2. Clique em **Create new secret key**
3. Dê um nome: "Document Management System"
4. Copie a chave (começa com `sk-...`)
5. ⚠️ **IMPORTANTE**: Salve em local seguro, não será mostrada novamente

### 2.3 Verificar Modelos Disponíveis

1. Certifique-se de ter acesso a:
   - `gpt-4` (para análise de documentos)
   - `gpt-3.5-turbo` (para sugestões de tags)

✅ **OpenAI configurado!**

---

## 3. Configurar Backend Python

### 3.1 Instalar Python

1. Baixe Python 3.11+ em [python.org](https://python.org)
2. Durante instalação, marque "Add Python to PATH"
3. Verifique instalação:
```bash
python --version
# Deve mostrar: Python 3.11.x ou superior
```

### 3.2 Configurar Ambiente Virtual

```bash
# Navegar para o diretório do backend
cd "C:\Users\Ricardo\Documents\Projeto Automacao\backend"

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Você verá (venv) no prompt
```

### 3.3 Instalar Dependências

```bash
# Com o ambiente virtual ativado
pip install -r requirements.txt

# Aguarde instalação de todos os pacotes
```

### 3.4 Configurar Variáveis de Ambiente

```bash
# Copiar template
copy .env.example .env

# Abrir .env em um editor de texto
notepad .env
```

Edite o arquivo `.env`:
```env
# Supabase (cole as credenciais do passo 1.2)
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=eyJhbGc...

# OpenAI (cole a API key do passo 2.2)
OPENAI_API_KEY=sk-...

# Application
APP_NAME=Document Management System
APP_VERSION=1.0.0
DEBUG=True

# CORS
FRONTEND_URL=http://localhost:3000
```

Salve e feche o arquivo.

### 3.5 Executar Backend

```bash
# Com ambiente virtual ativado
uvicorn main:app --reload

# Você verá:
# INFO:     Uvicorn running on http://127.0.0.1:8000
# INFO:     Application startup complete.
```

### 3.6 Verificar Backend

1. Abra navegador em: `http://localhost:8000`
2. Deve ver: `{"name": "Document Management System", ...}`
3. Acesse documentação: `http://localhost:8000/docs`
4. Deve ver interface Swagger com todos os endpoints

✅ **Backend configurado e rodando!**

---

## 4. Configurar Frontend

### 4.1 Instalar Node.js (se não tiver)

1. Baixe em [nodejs.org](https://nodejs.org)
2. Instale a versão LTS
3. Verifique:
```bash
node --version
npm --version
```

### 4.2 Servir Frontend

Abra um **NOVO terminal** (mantenha o backend rodando):

```bash
# Navegar para frontend
cd "C:\Users\Ricardo\Documents\Projeto Automacao\frontend"

# Servir com servidor local
npx -y serve .

# Você verá:
# Serving!
# - Local:    http://localhost:3000
```

### 4.3 Acessar Aplicação

1. Abra navegador em: `http://localhost:3000`
2. Você deve ver a interface completa do sistema
3. Dashboard deve carregar (pode estar vazio inicialmente)

✅ **Frontend configurado e rodando!**

---

## 5. Configurar n8n (Opcional)

### 5.1 Instalar n8n

```bash
# Instalar globalmente
npm install -g n8n
```

### 5.2 Executar n8n

Abra um **NOVO terminal**:

```bash
n8n start

# Acesse: http://localhost:5678
```

### 5.3 Importar Workflows

1. No n8n, clique em **Workflows** > **Import from File**
2. Selecione `n8n/workflows/document-processing.json`
3. Repita para os outros workflows:
   - `notifications.json`
   - `backup-export.json`

### 5.4 Configurar Credenciais

Para cada workflow:
1. Abra o workflow
2. Clique nos nós que precisam de credenciais (ícone de alerta)
3. Configure conforme necessário:
   - **HTTP Request**: URL do backend
   - **Email**: Configure SMTP
   - **Google Drive**: Conecte sua conta

### 5.5 Ativar Workflows

1. Abra cada workflow
2. Clique no toggle **Active** no canto superior direito
3. Workflow ficará verde quando ativo

✅ **n8n configurado!**

---

## 6. Verificação e Testes

### 6.1 Teste de Upload

1. No frontend (`http://localhost:3000`)
2. Arraste um arquivo PDF para a área de upload
3. Marque "Analisar com IA"
4. Clique em "Selecionar Arquivos"
5. Aguarde o upload
6. Documento deve aparecer no grid

### 6.2 Teste de Edição

1. Clique no ícone ✏️ em um documento
2. Edite o título
3. Adicione tags (separadas por vírgula)
4. Clique em "Salvar"
5. Verifique que mudanças foram aplicadas

### 6.3 Teste de IA

1. Clique no ícone 🤖 em um documento
2. Aguarde análise
3. Revise sugestões da IA
4. Clique em "Aplicar Sugestões"
5. Verifique que metadados foram atualizados

### 6.4 Teste de Busca

1. Digite algo na barra de busca
2. Resultados devem filtrar em tempo real
3. Teste filtros de categoria e tipo
4. Limpe filtros e busca

### 6.5 Teste de Dashboard

1. Clique em "Atualizar" no header
2. Gráficos devem atualizar
3. Estatísticas devem refletir documentos atuais

### 6.6 Teste de API

1. Acesse `http://localhost:8000/docs`
2. Expanda `POST /api/documents/upload`
3. Clique em "Try it out"
4. Faça upload de um arquivo
5. Clique em "Execute"
6. Verifique resposta 200 OK

✅ **Tudo funcionando!**

---

## 🎉 Próximos Passos

Agora que tudo está configurado:

1. **Explore a aplicação**: Faça upload de vários documentos
2. **Teste workflows n8n**: Configure notificações e backups
3. **Customize**: Modifique cores, categorias, etc.
4. **Expanda**: Adicione novas features conforme necessário

---

## ❓ Troubleshooting

### Backend não inicia
- Verifique se ambiente virtual está ativado
- Confirme que `.env` está configurado
- Verifique logs de erro no terminal

### Frontend não carrega dados
- Confirme que backend está rodando em `localhost:8000`
- Verifique console do navegador (F12) para erros
- Confirme CORS configurado no backend

### IA não funciona
- Verifique `OPENAI_API_KEY` no `.env`
- Confirme que tem créditos na conta OpenAI
- Veja logs do backend para erros da API

### Supabase connection error
- Verifique `SUPABASE_URL` e `SUPABASE_KEY`
- Confirme que schema SQL foi executado
- Teste conexão no Supabase dashboard

---

**Precisa de ajuda?** Consulte `README.md` ou `docs/API.md`
