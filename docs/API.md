# 📚 API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication
Currently, the API does not require authentication. In production, implement authentication using Supabase Auth or JWT tokens.

---

## Endpoints

### 📄 Documents

#### Upload Document
```http
POST /api/documents/upload
Content-Type: multipart/form-data

Body:
- file: File (required)

Response: 200 OK
{
  "success": true,
  "message": "Document uploaded successfully",
  "document": {
    "id": "uuid",
    "title": "filename.pdf",
    "file_name": "filename.pdf",
    "file_type": "pdf",
    "file_size": 1024000,
    "file_url": "https://...",
    "category": "Geral",
    "tags": [],
    "author": null,
    "description": null,
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z"
  }
}
```

#### Upload with AI Analysis
```http
POST /api/documents/analyze-upload
Content-Type: multipart/form-data

Body:
- file: File (required)

Response: 200 OK
{
  "success": true,
  "message": "Document uploaded and analyzed successfully",
  "document": {
    "id": "uuid",
    "title": "AI Suggested Title",
    "author": "AI Suggested Author",
    "category": "Técnico",
    "tags": ["ai", "generated", "tags"],
    "description": "AI generated summary...",
    ...
  }
}
```

#### List Documents
```http
GET /api/documents?category=Financeiro&file_type=pdf&search=relatorio&limit=50&offset=0

Query Parameters:
- category (optional): Filter by category
- file_type (optional): Filter by file type
- search (optional): Search in title, author, description
- limit (optional, default: 50): Number of results
- offset (optional, default: 0): Pagination offset

Response: 200 OK
[
  {
    "id": "uuid",
    "title": "Document Title",
    ...
  }
]
```

#### Get Document
```http
GET /api/documents/{id}

Response: 200 OK
{
  "id": "uuid",
  "title": "Document Title",
  ...
}

Response: 404 Not Found
{
  "detail": "Document not found"
}
```

#### Update Document
```http
PUT /api/documents/{id}
Content-Type: application/json

Body:
{
  "title": "New Title",
  "author": "Author Name",
  "category": "Financeiro",
  "tags": ["tag1", "tag2"],
  "description": "Updated description"
}

Note: All fields are optional. Only provided fields will be updated.

Response: 200 OK
{
  "id": "uuid",
  "title": "New Title",
  ...
}
```

#### Delete Document
```http
DELETE /api/documents/{id}

Response: 200 OK
{
  "success": true,
  "message": "Document deleted successfully"
}
```

#### Analyze Document with AI
```http
POST /api/documents/{id}/analyze

Response: 200 OK
{
  "suggested_title": "AI Suggested Title",
  "suggested_author": "Author Name",
  "suggested_category": "Técnico",
  "suggested_tags": ["tag1", "tag2", "tag3"],
  "summary": "AI generated summary of the document...",
  "confidence": 0.85
}
```

---

### 📊 Analytics

#### Get Statistics
```http
GET /api/analytics/stats

Response: 200 OK
{
  "total_documents": 42,
  "total_size": 104857600,
  "categories": [
    {
      "category": "Financeiro",
      "count": 15,
      "percentage": 35.71
    },
    ...
  ],
  "top_tags": [
    {
      "tag": "relatório",
      "count": 12
    },
    ...
  ],
  "timeline": [
    {
      "date": "2025-01-01",
      "count": 5
    },
    ...
  ],
  "documents_by_type": {
    "pdf": 20,
    "docx": 15,
    "xlsx": 7
  }
}
```

---

## Data Models

### Document
```typescript
{
  id: string (UUID)
  title: string
  author: string | null
  category: "Financeiro" | "RH" | "Técnico" | "Marketing" | "Legal" | "Geral"
  tags: string[]
  description: string | null
  file_name: string
  file_type: string
  file_size: number (bytes)
  file_url: string
  created_at: string (ISO 8601)
  updated_at: string (ISO 8601)
}
```

### AI Analysis Response
```typescript
{
  suggested_title: string | null
  suggested_author: string | null
  suggested_category: string | null
  suggested_tags: string[]
  summary: string | null
  confidence: number (0.0 to 1.0)
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Validation error message"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "detail": "Error details"
}
```

---

## Rate Limiting

Currently, there are no rate limits. In production, implement rate limiting using:
- FastAPI middleware
- Redis for distributed rate limiting
- API Gateway (AWS, Cloudflare)

---

## Interactive Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation where you can:
- View all endpoints
- Test API calls directly
- See request/response schemas
- Download OpenAPI spec

Alternative: `http://localhost:8000/redoc` for ReDoc documentation.
