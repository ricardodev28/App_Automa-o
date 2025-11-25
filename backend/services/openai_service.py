from openai import OpenAI
from typing import Dict, Any, Optional, List
import logging
import json
from config import settings
from models import CategoryEnum, AIAnalysisResponse

logger = logging.getLogger(__name__)


class OpenAIService:
    """Service for OpenAI API interactions."""
    
    def __init__(self):
        """Initialize OpenAI client."""
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.cache: Dict[str, AIAnalysisResponse] = {}
    
    async def analyze_document(
        self,
        file_name: str,
        file_type: str,
        content_preview: Optional[str] = None
    ) -> AIAnalysisResponse:
        """
        Analyze a document and extract metadata using GPT-4.
        
        Args:
            file_name: Name of the file
            file_type: Type of the file (e.g., 'pdf', 'docx')
            content_preview: Optional preview of document content
        
        Returns:
            AIAnalysisResponse with suggested metadata
        """
        # Check cache
        cache_key = f"{file_name}_{file_type}"
        if cache_key in self.cache:
            logger.info(f"Using cached analysis for {file_name}")
            return self.cache[cache_key]
        
        try:
            # Build prompt
            prompt = self._build_analysis_prompt(file_name, file_type, content_preview)
            
            # Call GPT-4
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert document analyst. Analyze documents and extract metadata accurately."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            # Parse response
            result = self._parse_gpt_response(response.choices[0].message.content)
            
            # Cache result
            self.cache[cache_key] = result
            
            return result
        except Exception as e:
            logger.error(f"Error analyzing document with OpenAI: {e}")
            # Return default response on error
            return AIAnalysisResponse(
                suggested_title=file_name,
                suggested_category=CategoryEnum.GERAL,
                suggested_tags=[],
                confidence=0.0
            )
    
    def _build_analysis_prompt(
        self,
        file_name: str,
        file_type: str,
        content_preview: Optional[str]
    ) -> str:
        """Build the analysis prompt for GPT-4."""
        prompt = f"""Analyze this document and extract metadata:

File Name: {file_name}
File Type: {file_type}
"""
        
        if content_preview:
            prompt += f"\nContent Preview:\n{content_preview[:500]}\n"
        
        prompt += f"""
Based on the file name{' and content' if content_preview else ''}, provide:

1. A clear, descriptive title (max 100 chars)
2. Suggested author (if identifiable, otherwise null)
3. Category (choose ONE from: Financeiro, RH, Técnico, Marketing, Legal, Geral)
4. 3-5 relevant tags
5. A brief summary (max 200 chars)
6. Confidence score (0.0 to 1.0)

Respond ONLY with valid JSON in this exact format:
{{
    "title": "Document Title",
    "author": "Author Name or null",
    "category": "Category",
    "tags": ["tag1", "tag2", "tag3"],
    "summary": "Brief summary",
    "confidence": 0.85
}}
"""
        return prompt
    
    def _parse_gpt_response(self, response_text: str) -> AIAnalysisResponse:
        """Parse GPT-4 response into AIAnalysisResponse."""
        try:
            # Extract JSON from response
            response_text = response_text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith("```"):
                lines = response_text.split("\n")
                response_text = "\n".join(lines[1:-1])
            
            data = json.loads(response_text)
            
            # Map category string to enum
            category_str = data.get("category", "Geral")
            category = self._map_category(category_str)
            
            return AIAnalysisResponse(
                suggested_title=data.get("title"),
                suggested_author=data.get("author"),
                suggested_category=category,
                suggested_tags=data.get("tags", []),
                summary=data.get("summary"),
                confidence=data.get("confidence", 0.5)
            )
        except Exception as e:
            logger.error(f"Error parsing GPT response: {e}")
            logger.debug(f"Response text: {response_text}")
            # Return minimal valid response
            return AIAnalysisResponse(
                suggested_category=CategoryEnum.GERAL,
                suggested_tags=[],
                confidence=0.0
            )
    
    def _map_category(self, category_str: str) -> CategoryEnum:
        """Map category string to CategoryEnum."""
        category_map = {
            "financeiro": CategoryEnum.FINANCEIRO,
            "rh": CategoryEnum.RH,
            "técnico": CategoryEnum.TECNICO,
            "tecnico": CategoryEnum.TECNICO,
            "marketing": CategoryEnum.MARKETING,
            "legal": CategoryEnum.LEGAL,
            "geral": CategoryEnum.GERAL,
        }
        
        return category_map.get(category_str.lower(), CategoryEnum.GERAL)
    
    async def suggest_tags(self, title: str, description: Optional[str] = None) -> List[str]:
        """Suggest tags based on title and description."""
        try:
            prompt = f"Suggest 5 relevant tags for this document:\nTitle: {title}"
            if description:
                prompt += f"\nDescription: {description}"
            
            prompt += "\n\nRespond with ONLY a JSON array of tags, e.g., [\"tag1\", \"tag2\", \"tag3\"]"
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that suggests relevant tags."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=100
            )
            
            tags_text = response.choices[0].message.content.strip()
            tags = json.loads(tags_text)
            return tags[:5]  # Limit to 5 tags
        except Exception as e:
            logger.error(f"Error suggesting tags: {e}")
            return []
    
    def clear_cache(self):
        """Clear the analysis cache."""
        self.cache.clear()
        logger.info("OpenAI cache cleared")


# Global service instance
openai_service = OpenAIService()
