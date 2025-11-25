from fastapi import APIRouter, HTTPException
import logging
from models import AnalyticsResponse
from services.supabase_service import supabase_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/stats", response_model=AnalyticsResponse)
async def get_analytics():
    """
    Get comprehensive analytics about all documents.
    
    Returns:
    - Total number of documents
    - Total storage size
    - Distribution by category
    - Top tags
    - Timeline of document creation
    - Distribution by file type
    """
    try:
        stats = await supabase_service.get_analytics()
        return AnalyticsResponse(**stats)
    except Exception as e:
        logger.error(f"Error getting analytics: {e}")
        raise HTTPException(status_code=500, detail=str(e))
