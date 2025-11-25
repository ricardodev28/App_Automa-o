# 📚 Sistema de Gestão de Documentos Inteligente

> Sistema completo de gestão de documentos com IA, automação e analytics - demonstrando organização de dados como base para soluções avançadas de automação.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-orange.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991.svg)

---

## 🎯 Visão Geral

Este projeto demonstra como a **organização e padronização de dados** é o primeiro passo essencial para qualquer solução avançada de automação ou IA. 

### O que este sistema faz?

Um sistema completo de gestão documental que permite:

- ✅ **Upload inteligente** de documentos com drag & drop
- 🤖 **Análise automática com IA** (GPT-4) para extração de metadados
- 📊 **Dashboard analítico** com gráficos e estatísticas em tempo real
- 🔄 **Automação de workflows** com n8n (notificações, backups, processamento)
- 🔍 **Busca avançada** com filtros por categoria, tipo e texto completo
- 📈 **API REST completa** com documentação interativa (Swagger)
- 💾 **Armazenamento em nuvem** com Supabase (PostgreSQL + Storage)

### Por que este projeto é útil?

- **Demonstração prática** de arquitetura moderna full-stack
- **Integração real** com serviços de IA (OpenAI) e banco de dados (Supabase)
- **Código limpo e bem documentado** seguindo boas práticas
- **Pronto para produção** com segurança, validação e tratamento de erros
- **Base sólida** para expansão e customização

---

## 🛠️ Stack Técnica

### Backend
- **Python 3.11+** - Linguagem moderna e eficiente
- **FastAPI** - Framework web assíncrono de alta performance
- **Supabase** - Backend-as-a-Service (PostgreSQL + Storage + Auth)
- **OpenAI API** - GPT-4 para análise inteligente de documentos
- **Pydantic** - Validação de dados e serialização
- **Uvicorn** - Servidor ASGI de alta performance

### Frontend
- **JavaScript ES6+** - Vanilla JS moderno (sem frameworks pesados)
- **HTML5/CSS3** - Semântico e acessível
- **Chart.js** - Visualizações de dados interativas
- **Design System** - Gradientes, glassmorphism, animações suaves
- **Responsivo** - Mobile-first design

### Banco de Dados
- **PostgreSQL** (via Supabase) - Banco relacional robusto
- **Supabase Storage** - Armazenamento de arquivos em nuvem
- **Row Level Security (RLS)** - Segurança em nível de linha
- **Full-text Search** - Busca otimizada em português

### Automação
- **n8n** - Plataforma de automação de workflows
- **Webhooks** - Integração em tempo real
- **Scheduled Jobs** - Tarefas agendadas (backups, relatórios)

---

## 📁 Estrutura do Projeto

```
Projeto Automacao/
├── backend/                      # API Python FastAPI
│   ├── main.py                   # Aplicação principal e configuração CORS
│   ├── config.py                 # Configurações e variáveis de ambiente
│   ├── models.py                 # Modelos Pydantic (validação de dados)
│   ├── .env.example              # Exemplo de variáveis de ambiente
│   ├── requirements.txt          # Dependências Python
│   │
│   ├── routes/                   # Endpoints da API
│   │   ├── __init__.py
│   │   ├── documents.py          # CRUD de documentos + upload
│   │   └── analytics.py          # Estatísticas e métricas
│   │
│   └── services/                 # Lógica de negócio
│       ├── __init__.py
│       ├── supabase_service.py   # Integração com Supabase
│       └── openai_service.py     # Integração com OpenAI GPT-4
│
├── frontend/                     # Interface web
│   ├── index.html                # Página principal (SPA)
│   ├── styles.css                # Design system completo
│   │
│   └── js/                       # Módulos JavaScript
│       ├── config.js             # Configurações da API
│       ├── api.js                # Cliente HTTP para backend
│       ├── ui.js                 # Helpers de interface (toasts, modals)
│       ├── dashboard.js          # Gráficos e analytics
│       └── app.js                # Lógica principal da aplicação
│
├── database/                     # Scripts Supabase
│   ├── schema.sql                # Schema completo do banco
│   └── seed.sql                  # Dados de exemplo (opcional)
│
├── n8n/                          # Workflows de automação
│   ├── README.md                 # Instruções de configuração
│   └── workflows/
│       ├── document-processing.json   # Processamento automático
│       ├── notifications.json         # Notificações por email
│       └── backup-export.json         # Backup semanal
│
├── docs/                         # Documentação adicional
│   ├── API.md                    # Documentação detalhada da API
│   └── SETUP.md                  # Guia de configuração passo a passo
│
├── .gitignore                    # Arquivos ignorados pelo Git
└── README.md                     # Este arquivo
```

---

## 🚀 Guia de Instalação Completo

### Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- ✅ **Python 3.11 ou superior** - [Download](https://www.python.org/downloads/)
- ✅ **Node.js 16+** - [Download](https://nodejs.org/) (para servir o frontend)
- ✅ **Git** - [Download](https://git-scm.com/)
- ✅ **Conta Supabase** (gratuita) - [Criar conta](https://supabase.com)
- ✅ **API Key OpenAI** - [Obter chave](https://platform.openai.com/api-keys)

---

### 📦 Passo 1: Clonar o Repositório

```bash
git clone https://github.com/ricardodev28/App_Automa-o.git
cd "Projeto Automacao"
```

---

### 🗄️ Passo 2: Configurar Supabase

#### 2.1. Criar Projeto no Supabase

1. Acesse [supabase.com](https://supabase.com) e faça login
2. Clique em **"New Project"**
3. Preencha:
   - **Name**: `document-management` (ou nome de sua preferência)
   - **Database Password**: Crie uma senha forte
   - **Region**: Escolha a região mais próxima
4. Aguarde a criação do projeto (~2 minutos)

#### 2.2. Executar Schema do Banco de Dados

1. No painel do Supabase, vá em **SQL Editor** (menu lateral)
2. Clique em **"New Query"**
3. Copie todo o conteúdo do arquivo `database/schema.sql`
4. Cole no editor e clique em **"Run"**
5. ✅ Você verá a mensagem "Success. No rows returned"

**O que foi criado:**
- Tabela `categories` com 6 categorias padrão
- Tabela `documents` com todos os campos necessários
- Índices para otimização de buscas
- Triggers para atualização automática de timestamps
- Políticas de segurança (RLS)
- Views para estatísticas

#### 2.3. Criar Storage Bucket

1. No Supabase, vá em **Storage** (menu lateral)
2. Clique em **"Create a new bucket"**
3. Preencha:
   - **Name**: `documents`
   - **Public bucket**: ✅ Marque esta opção
4. Clique em **"Create bucket"**

#### 2.4. Obter Credenciais

1. No Supabase, vá em **Settings** → **API**
2. Copie:
   - **Project URL** (ex: `https://xxxxx.supabase.co`)
   - **anon public** key (chave longa que começa com `eyJ...`)

---

### ⚙️ Passo 3: Configurar Backend

#### 3.1. Criar Ambiente Virtual Python

```bash
# Navegar para o backend
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

#### 3.2. Instalar Dependências

```bash
pip install -r requirements.txt
```

**Dependências instaladas:**
- `fastapi` - Framework web
- `uvicorn[standard]` - Servidor ASGI
- `supabase` - Cliente Supabase
- `openai` - Cliente OpenAI
- `pydantic` - Validação de dados
- `python-dotenv` - Variáveis de ambiente
- `aiofiles` - Upload de arquivos assíncrono

#### 3.3. Configurar Variáveis de Ambiente

```bash
# Copiar arquivo de exemplo
copy .env.example .env

# Editar o arquivo .env com suas credenciais
```

**Abra o arquivo `.env` e preencha:**

```env
# Supabase Configuration
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anon-aqui

# OpenAI Configuration
OPENAI_API_KEY=sk-proj-sua-chave-openai-aqui

# Application Settings
APP_NAME="Document Management System"
APP_VERSION="1.0.0"
DEBUG=True

# CORS Settings (Frontend URL)
FRONTEND_URL=http://localhost:3000
```

⚠️ **Importante:** Nunca compartilhe suas chaves de API!

#### 3.4. Testar Configuração

```bash
# Testar se as variáveis foram carregadas
python -c "from config import settings; print('✅ Configuração OK!')"
```

#### 3.5. Executar Servidor Backend

```bash
uvicorn main:app --reload
```

✅ **Sucesso!** O backend estará rodando em:
- API: `http://localhost:8000`
- Documentação interativa: `http://localhost:8000/docs`
- Documentação alternativa: `http://localhost:8000/redoc`

---

### 🎨 Passo 4: Configurar Frontend

Abra um **novo terminal** (mantenha o backend rodando):

```bash
# Navegar para o frontend
cd frontend

# Servir com servidor local
npx -y serve .
```

Ou use qualquer servidor HTTP de sua preferência:

```bash
# Alternativa 1: Python
python -m http.server 3000

# Alternativa 2: Node.js http-server
npx http-server -p 3000
```

✅ **Sucesso!** O frontend estará disponível em:
- Interface: `http://localhost:3000`

---

### 🔄 Passo 5: (Opcional) Configurar n8n

Para automação de workflows:

```bash
# Instalar n8n globalmente
npm install -g n8n

# Executar n8n
n8n start
```

Acesse `http://localhost:5678` e importe os workflows de `n8n/workflows/`

Veja `n8n/README.md` para instruções detalhadas.

---

## 📖 Como Usar o Sistema

### 1️⃣ Upload de Documentos

**Método 1: Drag & Drop**
1. Arraste um ou mais arquivos para a área de upload
2. Marque ✅ "Analisar com IA" se quiser análise automática
3. Aguarde o upload e processamento

**Método 2: Seleção Manual**
1. Clique em "Selecionar Arquivos"
2. Escolha os arquivos desejados
3. Confirme o upload

**Formatos suportados:**
- Documentos: PDF, DOCX, DOC, TXT
- Planilhas: XLSX, XLS, CSV
- Apresentações: PPTX, PPT
- Imagens: JPG, JPEG, PNG, GIF

### 2️⃣ Visualizar Documentos

Os documentos aparecem em cards com:
- 📄 Ícone do tipo de arquivo
- 📝 Título e descrição
- 👤 Autor
- 📅 Data de criação
- 💾 Tamanho do arquivo
- 🏷️ Tags
- 📁 Categoria (com cor)

### 3️⃣ Editar Metadados

1. Clique no ícone ✏️ no card do documento
2. Edite os campos:
   - **Título**: Nome descritivo
   - **Autor**: Nome do criador
   - **Categoria**: Financeiro, RH, Técnico, Marketing, Legal, Geral
   - **Tags**: Palavras-chave separadas por vírgula
   - **Descrição**: Resumo do conteúdo
3. Clique em "Salvar"

### 4️⃣ Análise com IA (GPT-4)

1. Clique no ícone 🤖 no card do documento
2. Aguarde a análise (~5-10 segundos)
3. Revise as sugestões:
   - Título sugerido
   - Autor identificado
   - Categoria recomendada
   - Tags relevantes
   - Resumo do conteúdo
   - Nível de confiança (%)
4. Clique em "Aplicar Sugestões" ou "Fechar"

**Dica:** A análise com IA é cacheada para economizar custos!

### 5️⃣ Buscar e Filtrar

**Busca por texto:**
- Digite na barra de busca
- Pesquisa em: título, autor, descrição
- Resultados em tempo real

**Filtros:**
- **Por categoria**: Selecione no dropdown
- **Por tipo de arquivo**: PDF, DOCX, etc.
- **Combinação**: Use busca + filtros juntos

### 6️⃣ Dashboard Analytics

Visualize estatísticas em tempo real:

**Cards de métricas:**
- 📄 Total de documentos
- 💾 Armazenamento usado (MB/GB)
- 🏷️ Tags únicas
- 📁 Categorias ativas

**Gráficos:**
- 📊 Distribuição por categoria (pizza)
- 🏷️ Tags mais usadas (barras)

Clique em "🔄 Atualizar" para recarregar os dados.

### 7️⃣ Excluir Documentos

1. Clique no ícone 🗑️ no card do documento
2. Confirme a exclusão
3. O arquivo será removido do storage e do banco

⚠️ **Atenção:** Esta ação é irreversível!

---

## 🔌 Documentação da API

### Endpoints Disponíveis

#### **Documentos**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/documents/upload` | Upload simples de arquivo |
| `POST` | `/api/documents/analyze-upload` | Upload + análise com IA |
| `GET` | `/api/documents` | Listar documentos (com filtros) |
| `GET` | `/api/documents/{id}` | Obter documento específico |
| `PUT` | `/api/documents/{id}` | Atualizar metadados |
| `DELETE` | `/api/documents/{id}` | Excluir documento |
| `POST` | `/api/documents/{id}/analyze` | Analisar documento com IA |

#### **Analytics**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/analytics/stats` | Estatísticas completas |

### Exemplos de Uso

#### Listar documentos com filtros

```bash
GET /api/documents?category=Financeiro&file_type=pdf&search=contrato&limit=10
```

#### Upload com análise IA

```bash
POST /api/documents/analyze-upload
Content-Type: multipart/form-data

file: [arquivo]
```

#### Atualizar metadados

```bash
PUT /api/documents/{id}
Content-Type: application/json

{
  "title": "Novo Título",
  "author": "João Silva",
  "category": "Técnico",
  "tags": ["python", "api", "fastapi"],
  "description": "Documentação técnica da API"
}
```

### Documentação Interativa

Acesse `http://localhost:8000/docs` para:
- ✅ Ver todos os endpoints
- ✅ Testar requisições diretamente
- ✅ Ver schemas de dados
- ✅ Copiar exemplos de código

---

## 🤖 Automação com n8n

O projeto inclui **3 workflows prontos**:

### 1. Document Processing
Processa automaticamente documentos após upload:
- Webhook recebe notificação de novo documento
- Extrai metadados com IA
- Atualiza banco de dados
- Envia notificação

### 2. Daily Notifications
Envia resumo diário por email:
- Executa todo dia às 9h
- Coleta estatísticas do dia anterior
- Formata email HTML
- Envia para lista de destinatários

### 3. Weekly Backup
Backup semanal para cloud storage:
- Executa toda segunda-feira
- Exporta todos os documentos
- Compacta em ZIP
- Envia para Google Drive/Dropbox

**Configuração:** Veja `n8n/README.md`

---

## 🎨 Features Principais

### ✨ Interface Premium
- 🎨 Design moderno com gradientes vibrantes
- 💎 Glassmorphism e efeitos de profundidade
- ⚡ Animações suaves e micro-interações
- 📱 Totalmente responsivo (mobile-first)
- 🎯 Feedback visual para todas as ações
- 🌈 Paleta de cores harmoniosa

### 🤖 IA Integrada
- 🧠 GPT-4 para análise de documentos
- 🏷️ Categorização automática inteligente
- 📝 Extração de metadados (título, autor, tags)
- 📄 Geração de resumos
- 💰 Sistema de cache para reduzir custos
- 🎯 Nível de confiança nas sugestões

### 📊 Analytics em Tempo Real
- 📈 Gráficos interativos com Chart.js
- 📊 Distribuição por categoria
- 🏷️ Tags mais utilizadas
- 📅 Timeline de documentos
- 👥 Top autores
- 💾 Uso de armazenamento

### 🔍 Busca Avançada
- 🔎 Full-text search otimizado
- 🏷️ Filtros por categoria e tipo
- ⚡ Resultados em tempo real
- 📊 Ordenação customizável
- 🇧🇷 Suporte a português (stemming)

### 🔒 Segurança
- 🛡️ Row Level Security (RLS) no Supabase
- ✅ Validação de dados com Pydantic
- 🌐 CORS configurado corretamente
- 🔐 Environment variables para credenciais
- 🚫 Proteção contra SQL injection
- 📝 Logs de auditoria

---

## 🔧 Solução de Problemas

### Backend não inicia

**Erro:** `ModuleNotFoundError: No module named 'fastapi'`

**Solução:**
```bash
# Ative o ambiente virtual
venv\Scripts\activate

# Reinstale as dependências
pip install -r requirements.txt
```

---

**Erro:** `ValidationError: SUPABASE_URL field required`

**Solução:**
- Verifique se o arquivo `.env` existe em `backend/`
- Confirme que as variáveis estão preenchidas corretamente
- Não use espaços ao redor do `=`

---

### Frontend não conecta ao backend

**Erro:** `Failed to fetch` ou `CORS error`

**Solução:**
1. Verifique se o backend está rodando em `http://localhost:8000`
2. Confirme que `FRONTEND_URL` no `.env` está correto
3. Limpe o cache do navegador (Ctrl+Shift+Delete)

---

### Upload de arquivos falha

**Erro:** `413 Payload Too Large`

**Solução:**
- Limite de tamanho padrão: 50MB
- Para arquivos maiores, ajuste em `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    max_upload_size=100 * 1024 * 1024  # 100MB
)
```

---

### Análise com IA não funciona

**Erro:** `OpenAI API error: Invalid API key`

**Solução:**
1. Verifique se `OPENAI_API_KEY` está correto no `.env`
2. Confirme que a chave está ativa em [platform.openai.com](https://platform.openai.com)
3. Verifique se tem créditos disponíveis

---

### Supabase retorna erro 401

**Erro:** `Unauthorized`

**Solução:**
1. Verifique se `SUPABASE_KEY` é a chave **anon public** (não a service_role)
2. Confirme que as políticas RLS estão configuradas
3. Re-execute o `schema.sql` se necessário

---

## 📝 Próximos Passos e Melhorias

### Funcionalidades Planejadas

- [ ] **Autenticação de usuários** (Supabase Auth)
  - Login/Registro
  - Perfis de usuário
  - Documentos privados

- [ ] **OCR para PDFs e imagens**
  - Extrair texto de documentos escaneados
  - Busca em conteúdo de imagens

- [ ] **Versionamento de documentos**
  - Histórico de alterações
  - Restaurar versões antigas
  - Comparação de versões

- [ ] **Compartilhamento e permissões**
  - Compartilhar documentos por link
  - Controle de acesso (leitura/escrita)
  - Expiração de links

- [ ] **Integração com cloud storage**
  - Google Drive
  - Dropbox
  - OneDrive

- [ ] **Busca semântica com embeddings**
  - Busca por similaridade
  - Recomendações de documentos
  - Agrupamento automático

- [ ] **Assinatura digital**
  - Assinar documentos eletronicamente
  - Verificação de autenticidade

- [ ] **Templates de documentos**
  - Criar documentos a partir de templates
  - Editor integrado

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Este é um projeto de demonstração, mas você pode:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**

### Diretrizes

- Siga o estilo de código existente
- Adicione testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Descreva claramente as mudanças no PR

---

## 📄 Licença

**MIT License**

Copyright (c) 2024 Ricardo

Você é livre para:
- ✅ Usar comercialmente
- ✅ Modificar
- ✅ Distribuir
- ✅ Uso privado

Sob as condições:
- 📝 Incluir aviso de copyright
- 📝 Incluir cópia da licença

---

## 🙋 Suporte e Contato

### Documentação

1. **Documentação da API**: `http://localhost:8000/docs`
2. **Guia de Setup**: `docs/SETUP.md`
3. **Workflows n8n**: `n8n/README.md`

### Recursos Úteis

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação Supabase](https://supabase.com/docs)
- [Documentação OpenAI](https://platform.openai.com/docs)
- [Documentação n8n](https://docs.n8n.io/)

### Reportar Problemas

Encontrou um bug? Abra uma [issue no GitHub](https://github.com/ricardodev28/App_Automa-o/issues)

---

## 🌟 Agradecimentos

Este projeto foi desenvolvido como demonstração de:
- Arquitetura full-stack moderna
- Integração com serviços de IA
- Boas práticas de desenvolvimento
- Organização e padronização de dados

**Tecnologias utilizadas:**
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web Python
- [Supabase](https://supabase.com/) - Backend as a Service
- [OpenAI](https://openai.com/) - Inteligência Artificial
- [Chart.js](https://www.chartjs.org/) - Gráficos interativos
- [n8n](https://n8n.io/) - Automação de workflows

---

## 🚀 Próximos Passos de Configuração

Após clonar o repositório, siga estes passos para configurar e executar o projeto:

### 📋 Passo 1: Configurar Supabase (5 minutos)

#### 1.1. Criar Projeto no Supabase

1. **Acesse** [supabase.com](https://supabase.com) e faça login (ou crie uma conta gratuita)
2. **Clique** em **"New Project"**
3. **Preencha** os dados do projeto:
   - **Name**: `document-management` (ou nome de sua preferência)
   - **Database Password**: Crie uma senha forte e **guarde-a**
   - **Region**: Escolha a região mais próxima de você
4. **Aguarde** a criação do projeto (~2 minutos)

#### 1.2. Executar Schema do Banco de Dados

1. No painel do Supabase, vá em **SQL Editor** (menu lateral esquerdo)
2. Clique em **"New Query"**
3. Abra o arquivo `database/schema.sql` do projeto
4. **Copie todo o conteúdo** e cole no editor SQL
5. Clique em **"Run"** (ou pressione Ctrl+Enter)
6. ✅ Você verá a mensagem **"Success. No rows returned"**

**O que foi criado:**
- ✅ Tabela `categories` com 6 categorias padrão (Financeiro, RH, Técnico, Marketing, Legal, Geral)
- ✅ Tabela `documents` com todos os campos necessários
- ✅ Índices para otimização de buscas e filtros
- ✅ Triggers para atualização automática de timestamps
- ✅ Políticas de segurança (Row Level Security)
- ✅ Views para estatísticas e analytics

#### 1.3. Criar Storage Bucket para Arquivos

1. No Supabase, vá em **Storage** (menu lateral esquerdo)
2. Clique em **"Create a new bucket"**
3. Preencha:
   - **Name**: `documents` (exatamente este nome)
   - **Public bucket**: ✅ **Marque esta opção** (para permitir acesso aos arquivos)
4. Clique em **"Create bucket"**

#### 1.4. Obter Credenciais do Supabase

1. No Supabase, vá em **Settings** → **API** (menu lateral)
2. **Copie** as seguintes informações:
   - **Project URL** (ex: `https://xxxxx.supabase.co`)
   - **anon public** key (chave longa que começa com `eyJ...`)

⚠️ **Importante:** Guarde essas credenciais, você vai precisar no Passo 2!

---

### ⚙️ Passo 2: Configurar Backend (3 minutos)

#### 2.1. Criar Ambiente Virtual Python

Abra o terminal na pasta do projeto e execute:

```bash
# Navegar para o backend
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

💡 **Dica:** Você saberá que o ambiente está ativo quando ver `(venv)` no início da linha do terminal.

#### 2.2. Instalar Dependências Python

Com o ambiente virtual ativo, execute:

```bash
pip install -r requirements.txt
```

Isso instalará:
- ✅ `fastapi` - Framework web
- ✅ `uvicorn[standard]` - Servidor ASGI
- ✅ `supabase` - Cliente Supabase
- ✅ `openai` - Cliente OpenAI
- ✅ `pydantic` - Validação de dados
- ✅ `python-dotenv` - Variáveis de ambiente
- ✅ `aiofiles` - Upload de arquivos assíncrono

#### 2.3. Configurar Variáveis de Ambiente

```bash
# Copiar arquivo de exemplo
copy .env.example .env   # Windows
# ou
cp .env.example .env     # Linux/Mac
```

Agora **edite o arquivo `.env`** com suas credenciais:

```env
# Supabase Configuration
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anon-public-aqui

# OpenAI Configuration
OPENAI_API_KEY=sk-proj-sua-chave-openai-aqui

# Application Settings
APP_NAME="Document Management System"
APP_VERSION="1.0.0"
DEBUG=True

# CORS Settings (Frontend URL)
FRONTEND_URL=http://localhost:3000
```

**Como obter a OpenAI API Key:**
1. Acesse [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Faça login ou crie uma conta
3. Clique em **"Create new secret key"**
4. Copie a chave e cole no `.env`

⚠️ **Importante:** Nunca compartilhe suas chaves de API ou faça commit do arquivo `.env`!

#### 2.4. Testar Configuração

```bash
# Testar se as variáveis foram carregadas corretamente
python -c "from config import settings; print('✅ Configuração OK!')"
```

Se aparecer `✅ Configuração OK!`, está tudo certo!

#### 2.5. Executar Servidor Backend

```bash
uvicorn main:app --reload
```

✅ **Sucesso!** Você verá:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**URLs disponíveis:**
- 🌐 API: http://localhost:8000
- 📚 Documentação interativa: http://localhost:8000/docs
- 📖 Documentação alternativa: http://localhost:8000/redoc

⚠️ **Mantenha este terminal aberto** com o backend rodando!

---

### 🎨 Passo 3: Executar Frontend (1 minuto)

Abra um **novo terminal** (mantenha o backend rodando no outro):

```bash
# Navegar para o frontend
cd frontend

# Servir com servidor local
npx -y serve .
```

**Alternativas:**

```bash
# Opção 1: Python (se você tiver Python instalado)
python -m http.server 3000

# Opção 2: Node.js http-server
npx http-server -p 3000

# Opção 3: Live Server (VS Code extension)
# Clique com botão direito em index.html > Open with Live Server
```

✅ **Sucesso!** O frontend estará disponível em:
- 🌐 Interface: http://localhost:3000

---

### 🎯 Passo 4: Acessar e Testar o Sistema (2 minutos)

#### 4.1. Abrir a Aplicação

1. Abra seu navegador
2. Acesse: http://localhost:3000
3. Você verá a interface do **Sistema de Gestão de Documentos**

#### 4.2. Testar Upload de Documento

1. **Arraste um arquivo** para a área de upload (ou clique para selecionar)
2. Marque ✅ **"Analisar com IA"** (se quiser análise automática)
3. Aguarde o upload
4. ✅ O documento aparecerá no grid abaixo

**Formatos suportados:**
- 📄 Documentos: PDF, DOCX, DOC, TXT
- 📊 Planilhas: XLSX, XLS, CSV
- 📽️ Apresentações: PPTX, PPT
- 🖼️ Imagens: JPG, JPEG, PNG, GIF

#### 4.3. Testar Análise com IA

1. Clique no ícone **🤖** em qualquer documento
2. Aguarde a análise (~5-10 segundos)
3. Revise as sugestões de metadados
4. Clique em **"Aplicar Sugestões"** ou **"Fechar"**

#### 4.4. Explorar o Dashboard

1. Role a página para cima
2. Visualize as estatísticas:
   - 📄 Total de documentos
   - 💾 Armazenamento usado
   - 🏷️ Tags únicas
   - 📊 Gráficos de distribuição

#### 4.5. Testar Busca e Filtros

1. Digite algo na **barra de busca**
2. Use os **filtros** de categoria e tipo
3. Veja os resultados em tempo real

#### 4.6. Verificar a API

1. Acesse: http://localhost:8000/docs
2. Explore os endpoints disponíveis
3. Teste requisições diretamente na interface Swagger

---

### ✅ Checklist de Verificação

Após completar os 4 passos, verifique se tudo está funcionando:

- [ ] ✅ Supabase configurado (projeto criado, schema executado, bucket criado)
- [ ] ✅ Backend rodando em http://localhost:8000
- [ ] ✅ Frontend rodando em http://localhost:3000
- [ ] ✅ Upload de documentos funcionando
- [ ] ✅ Análise com IA funcionando (se configurou OpenAI)
- [ ] ✅ Dashboard exibindo estatísticas
- [ ] ✅ Busca e filtros funcionando
- [ ] ✅ Documentação da API acessível em /docs

---

### 🔧 Problemas Comuns e Soluções

#### ❌ Backend não inicia

**Erro:** `ModuleNotFoundError: No module named 'fastapi'`

**Solução:**
```bash
# Certifique-se de que o ambiente virtual está ativo
venv\Scripts\activate
# Reinstale as dependências
pip install -r requirements.txt
```

---

#### ❌ Frontend não conecta ao backend

**Erro:** `Failed to fetch` ou `CORS error`

**Solução:**
1. Verifique se o backend está rodando em http://localhost:8000
2. Confirme que `FRONTEND_URL` no `.env` está como `http://localhost:3000`
3. Limpe o cache do navegador (Ctrl+Shift+Delete)
4. Reinicie o backend

---

#### ❌ Análise com IA não funciona

**Erro:** `OpenAI API error`

**Solução:**
1. Verifique se `OPENAI_API_KEY` está correto no `.env`
2. Confirme que a chave está ativa em [platform.openai.com](https://platform.openai.com)
3. Verifique se tem créditos disponíveis na sua conta OpenAI
4. Reinicie o backend após alterar o `.env`

---

#### ❌ Upload de arquivos falha

**Erro:** `Error uploading file`

**Solução:**
1. Verifique se o bucket `documents` foi criado no Supabase Storage
2. Confirme que o bucket está marcado como **público**
3. Verifique se `SUPABASE_URL` e `SUPABASE_KEY` estão corretos
4. Teste a conexão com Supabase:
```bash
python -c "from services.supabase_service import supabase_service; print('✅ Supabase OK!')"
```

---

### 🎉 Pronto para Usar!

Agora você tem um sistema completo de gestão de documentos com:
- ✅ Upload e armazenamento em nuvem
- ✅ Análise inteligente com IA
- ✅ Dashboard com analytics
- ✅ API REST documentada
- ✅ Interface moderna e responsiva

**Próximas melhorias sugeridas:**
- 🔐 Adicionar autenticação de usuários
- 📝 Implementar OCR para PDFs
- 🔄 Configurar workflows n8n
- 📱 Criar app mobile
- 🌐 Deploy em produção (Vercel + Railway)

---

<div align="center">

**Desenvolvido com ❤️ como demonstração de organização de dados e automação**

⭐ Se este projeto foi útil, considere dar uma estrela!

[🐛 Reportar Bug](https://github.com/ricardodev28/App_Automa-o/issues) · 
[✨ Solicitar Feature](https://github.com/ricardodev28/App_Automa-o/issues) · 
[📖 Documentação](https://github.com/ricardodev28/App_Automa-o/wiki)

</div>
