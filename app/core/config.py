
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SimpleAI Voice Processor"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./simpleai.db"
    
    class Config:
        case_sensitive = True

settings = Settings()
