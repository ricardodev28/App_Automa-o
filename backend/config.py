from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Supabase
    supabase_url: str
    supabase_key: str
    
    # OpenAI
    openai_api_key: str
    
    # Application
    app_name: str = "Document Management System"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # CORS
    frontend_url: str = "http://localhost:3000"
    
    @property
    def cors_origins(self) -> List[str]:
        """Get list of allowed CORS origins."""
        return [
            self.frontend_url,
            "http://localhost:5000",
            "http://127.0.0.1:5000",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
