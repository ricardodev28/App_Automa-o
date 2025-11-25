from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from typing import Optional, List
import logging
import uuid
from datetime import datetime

from models import (
    Document,
    DocumentCreate,
    DocumentUpdate,
    UploadResponse,
    AIAnalysisRequest,
    AIAnalysisResponse
)
from services.supabase_service import supabase_service
from services.openai_service import openai_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a new document.
    
    The file will be uploaded to Supabase Storage and metadata will be stored in the database.
    """
    try:
        # Validate file
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        # Read file content
        content = await file.read()
        file_size = len(content)
        
        # Generate unique file path
        file_extension = file.filename.split(".")[-1] if "." in file.filename else ""
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        
        # Upload to Supabase Storage
        file_url = await supabase_service.upload_file(
            unique_filename,
            content,
            file.content_type or "application/octet-stream"
        )
        
        # Create document record
        document_data = DocumentCreate(
            title=file.filename,
            file_name=file.filename,
            file_type=file_extension,
            file_size=file_size,
            file_url=file_url,
            tags=[],
            description=None
        )
        
        doc = await supabase_service.create_document(document_data)
        
        return UploadResponse(
            success=True,
            message="Document uploaded successfully",
            document=Document(**doc)
        )
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("", response_model=List[Document])
async def get_documents(
    category: Optional[str] = Query(None, description="Filter by category"),
    file_type: Optional[str] = Query(None, description="Filter by file type"),
    search: Optional[str] = Query(None, description="Search in title, author, description"),
    limit: int = Query(50, ge=1, le=100, description="Number of documents to return"),
    offset: int = Query(0, ge=0, description="Number of documents to skip")
):
    """
    Get all documents with optional filters.
    
    Supports filtering by category, file type, and text search.
    Results are paginated and ordered by creation date (newest first).
    """
    try:
        docs = await supabase_service.get_documents(
            category=category,
            file_type=file_type,
            search=search,
            limit=limit,
            offset=offset
        )
        return [Document(**doc) for doc in docs]
    except Exception as e:
        logger.error(f"Error getting documents: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{document_id}", response_model=Document)
async def get_document(document_id: str):
    """Get a specific document by ID."""
    try:
        doc = await supabase_service.get_document(document_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return Document(**doc)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting document: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{document_id}", response_model=Document)
async def update_document(document_id: str, update_data: DocumentUpdate):
    """
    Update a document's metadata.
    
    Only provided fields will be updated. Others will remain unchanged.
    """
    try:
        doc = await supabase_service.update_document(document_id, update_data)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return Document(**doc)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating document: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{document_id}")
async def delete_document(document_id: str):
    """
    Delete a document.
    
    This will remove both the database record and the file from storage.
    """
    try:
        success = await supabase_service.delete_document(document_id)
        if not success:
            raise HTTPException(status_code=404, detail="Document not found")
        return {"success": True, "message": "Document deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting document: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{document_id}/analyze", response_model=AIAnalysisResponse)
async def analyze_document(document_id: str):
    """
    Analyze a document using OpenAI to extract metadata.
    
    This will use GPT-4 to suggest:
    - Title
    - Author
    - Category
    - Tags
    - Summary
    
    The analysis is cached to reduce API costs.
    """
    try:
        # Get document
        doc = await supabase_service.get_document(document_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        
        # Analyze with OpenAI
        analysis = await openai_service.analyze_document(
            file_name=doc["file_name"],
            file_type=doc["file_type"],
            content_preview=doc.get("description")
        )
        
        return analysis
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error analyzing document: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze-upload", response_model=UploadResponse)
async def upload_and_analyze(file: UploadFile = File(...)):
    """
    Upload a document and automatically analyze it with AI.
    
    This combines upload and AI analysis in a single request.
    The document will be created with AI-suggested metadata.
    """
    try:
        # First upload the document
        upload_result = await upload_document(file)
        
        if not upload_result.document:
            return upload_result
        
        # Analyze with AI
        analysis = await openai_service.analyze_document(
            file_name=upload_result.document.file_name,
            file_type=upload_result.document.file_type
        )
        
        # Update document with AI suggestions
        update_data = DocumentUpdate(
            title=analysis.suggested_title or upload_result.document.title,
            author=analysis.suggested_author,
            category=analysis.suggested_category,
            tags=analysis.suggested_tags,
            description=analysis.summary
        )
        
        updated_doc = await supabase_service.update_document(
            upload_result.document.id,
            update_data
        )
        
        return UploadResponse(
            success=True,
            message="Document uploaded and analyzed successfully",
            document=Document(**updated_doc) if updated_doc else upload_result.document
        )
    except Exception as e:
        logger.error(f"Error in upload and analyze: {e}")
        raise HTTPException(status_code=500, detail=str(e))
