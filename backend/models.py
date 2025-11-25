from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class CategoryEnum(str, Enum):
    """Document categories."""
    FINANCEIRO = "Financeiro"
    RH = "RH"
    TECNICO = "Técnico"
    MARKETING = "Marketing"
    LEGAL = "Legal"
    GERAL = "Geral"


class DocumentBase(BaseModel):
    """Base document model."""
    title: str = Field(..., min_length=1, max_length=255)
    author: Optional[str] = Field(None, max_length=100)
    category: CategoryEnum = CategoryEnum.GERAL
    tags: List[str] = Field(default_factory=list)
    description: Optional[str] = None


class DocumentCreate(DocumentBase):
    """Model for creating a new document."""
    file_name: str
    file_type: str
    file_size: int
    file_url: str


class DocumentUpdate(BaseModel):
    """Model for updating document metadata."""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, max_length=100)
    category: Optional[CategoryEnum] = None
    tags: Optional[List[str]] = None
    description: Optional[str] = None


class Document(DocumentBase):
    """Complete document model with all fields."""
    id: str
    file_name: str
    file_type: str
    file_size: int
    file_url: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class AIAnalysisRequest(BaseModel):
    """Request model for AI analysis."""
    document_id: str
    analyze_content: bool = True
    extract_metadata: bool = True


class AIAnalysisResponse(BaseModel):
    """Response model for AI analysis."""
    suggested_title: Optional[str] = None
    suggested_author: Optional[str] = None
    suggested_category: Optional[CategoryEnum] = None
    suggested_tags: List[str] = Field(default_factory=list)
    summary: Optional[str] = None
    confidence: float = Field(ge=0.0, le=1.0)


class CategoryStats(BaseModel):
    """Statistics for a category."""
    category: str
    count: int
    percentage: float


class TagStats(BaseModel):
    """Statistics for a tag."""
    tag: str
    count: int


class TimelineData(BaseModel):
    """Timeline data point."""
    date: str
    count: int


class AnalyticsResponse(BaseModel):
    """Analytics response model."""
    total_documents: int
    total_size: int
    categories: List[CategoryStats]
    top_tags: List[TagStats]
    timeline: List[TimelineData]
    documents_by_type: dict


class UploadResponse(BaseModel):
    """Response model for file upload."""
    success: bool
    message: str
    document: Optional[Document] = None


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    detail: Optional[str] = None
