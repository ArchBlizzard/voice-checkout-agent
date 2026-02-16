
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.api.endpoints import router as api_router
from app.db.database import engine, Base

# Create DB Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Configure Logging
setup_logging()

app.include_router(api_router, prefix="/calls", tags=["calls"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
