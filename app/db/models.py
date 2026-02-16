
from sqlalchemy import Column, Integer, String, JSON, DateTime, Float
from app.db.database import Base
from datetime import datetime

class CallLog(Base):
    __tablename__ = "call_logs"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, unique=True, index=True)
    transcripts = Column(JSON)
    analyzers = Column(JSON)
    analysis_results = Column(JSON)
    summary = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime, nullable=True)

class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    stock_count = Column(Integer, default=0)
    price = Column(Float, default=0.0)

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, index=True)
    amount = Column(Float)
    pdf_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
