from supabase import create_client, Client
from typing import List, Optional, Dict, Any
from datetime import datetime
import logging
from config import settings
from models import Document, DocumentCreate, DocumentUpdate, CategoryEnum

logger = logging.getLogger(__name__)


class SupabaseService:
    """Service for interacting with Supabase."""
    
    def __init__(self):
        """Initialize Supabase client."""
        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_key
        )
        self.storage_bucket = "documents"
    
    async def create_document(self, document: DocumentCreate) -> Dict[str, Any]:
        """Create a new document in the database."""
        try:
            data = {
                "title": document.title,
                "author": document.author,
                "category": document.category.value,
                "tags": document.tags,
                "description": document.description,
                "file_name": document.file_name,
                "file_type": document.file_type,
                "file_size": document.file_size,
                "file_url": document.file_url,
            }
            
            result = self.client.table("documents").insert(data).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            logger.error(f"Error creating document: {e}")
            raise
    
    async def get_document(self, document_id: str) -> Optional[Dict[str, Any]]:
        """Get a document by ID."""
        try:
            result = self.client.table("documents").select("*").eq("id", document_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            logger.error(f"Error getting document: {e}")
            raise
    
    async def get_documents(
        self,
        category: Optional[str] = None,
        file_type: Optional[str] = None,
        search: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Get documents with optional filters."""
        try:
            query = self.client.table("documents").select("*")
            
            # Apply filters
            if category:
                query = query.eq("category", category)
            
            if file_type:
                query = query.eq("file_type", file_type)
            
            if search:
                # Search in title, author, and description
                query = query.or_(
                    f"title.ilike.%{search}%,"
                    f"author.ilike.%{search}%,"
                    f"description.ilike.%{search}%"
                )
            
            # Order by created_at descending
            query = query.order("created_at", desc=True)
            
            # Pagination
            query = query.range(offset, offset + limit - 1)
            
            result = query.execute()
            return result.data
        except Exception as e:
            logger.error(f"Error getting documents: {e}")
            raise
    
    async def update_document(
        self,
        document_id: str,
        update_data: DocumentUpdate
    ) -> Optional[Dict[str, Any]]:
        """Update a document's metadata."""
        try:
            # Build update dict with only provided fields
            data = {}
            if update_data.title is not None:
                data["title"] = update_data.title
            if update_data.author is not None:
                data["author"] = update_data.author
            if update_data.category is not None:
                data["category"] = update_data.category.value
            if update_data.tags is not None:
                data["tags"] = update_data.tags
            if update_data.description is not None:
                data["description"] = update_data.description
            
            if not data:
                return await self.get_document(document_id)
            
            data["updated_at"] = datetime.utcnow().isoformat()
            
            result = self.client.table("documents").update(data).eq("id", document_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            logger.error(f"Error updating document: {e}")
            raise
    
    async def delete_document(self, document_id: str) -> bool:
        """Delete a document."""
        try:
            # Get document to find file path
            doc = await self.get_document(document_id)
            if not doc:
                return False
            
            # Delete from storage if file exists
            if doc.get("file_url"):
                file_path = doc["file_url"].split("/")[-1]
                try:
                    self.client.storage.from_(self.storage_bucket).remove([file_path])
                except Exception as e:
                    logger.warning(f"Error deleting file from storage: {e}")
            
            # Delete from database
            self.client.table("documents").delete().eq("id", document_id).execute()
            return True
        except Exception as e:
            logger.error(f"Error deleting document: {e}")
            raise
    
    async def upload_file(self, file_path: str, file_data: bytes, content_type: str) -> str:
        """Upload a file to Supabase Storage."""
        try:
            result = self.client.storage.from_(self.storage_bucket).upload(
                file_path,
                file_data,
                {"content-type": content_type}
            )
            
            # Get public URL
            public_url = self.client.storage.from_(self.storage_bucket).get_public_url(file_path)
            return public_url
        except Exception as e:
            logger.error(f"Error uploading file: {e}")
            raise
    
    async def get_analytics(self) -> Dict[str, Any]:
        """Get analytics data."""
        try:
            # Get all documents
            all_docs = self.client.table("documents").select("*").execute()
            docs = all_docs.data
            
            if not docs:
                return {
                    "total_documents": 0,
                    "total_size": 0,
                    "categories": [],
                    "top_tags": [],
                    "timeline": [],
                    "documents_by_type": {}
                }
            
            # Calculate statistics
            total_size = sum(doc.get("file_size", 0) for doc in docs)
            
            # Category distribution
            category_counts = {}
            for doc in docs:
                cat = doc.get("category", "Geral")
                category_counts[cat] = category_counts.get(cat, 0) + 1
            
            categories = [
                {
                    "category": cat,
                    "count": count,
                    "percentage": round((count / len(docs)) * 100, 2)
                }
                for cat, count in category_counts.items()
            ]
            
            # Tag statistics
            tag_counts = {}
            for doc in docs:
                for tag in doc.get("tags", []):
                    tag_counts[tag] = tag_counts.get(tag, 0) + 1
            
            top_tags = [
                {"tag": tag, "count": count}
                for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            ]
            
            # File type distribution
            type_counts = {}
            for doc in docs:
                file_type = doc.get("file_type", "unknown")
                type_counts[file_type] = type_counts.get(file_type, 0) + 1
            
            # Timeline (last 30 days)
            timeline_counts = {}
            for doc in docs:
                created = doc.get("created_at", "")
                if created:
                    date = created.split("T")[0]
                    timeline_counts[date] = timeline_counts.get(date, 0) + 1
            
            timeline = [
                {"date": date, "count": count}
                for date, count in sorted(timeline_counts.items())
            ]
            
            return {
                "total_documents": len(docs),
                "total_size": total_size,
                "categories": categories,
                "top_tags": top_tags,
                "timeline": timeline,
                "documents_by_type": type_counts
            }
        except Exception as e:
            logger.error(f"Error getting analytics: {e}")
            raise


# Global service instance
supabase_service = SupabaseService()
