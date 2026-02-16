
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TranscriptUser(str, Enum):
    AGENT = "agent"
    USER = "user"

class TranscriptSegment(BaseModel):
    id: int
    text: str
    user: TranscriptUser
    timestamp: float

class AnalyzerType(str, Enum):
    INTENT_RECOGNITION = "intent_recognition"
    SENTIMENT_ANALYSIS = "sentiment_analysis"
    ENTITY_EXTRACTION = "entity_extraction"
    CHECKOUT_COMPLETION = "checkout_completion"

class Analyzer(BaseModel):
    id: str
    type: AnalyzerType
    instruction: str

class AnalysisResult(BaseModel):
    analyzer_id: str
    result: Dict[str, Any]
    confidence_score: float

class CallPayload(BaseModel):
    call_id: str
    transcripts: List[TranscriptSegment]
    analyzers: List[Analyzer] = Field(default_factory=list)
    analysis_results: List[AnalysisResult] = Field(default_factory=list)
    summary: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class CheckoutItem(BaseModel):
    product_name: str
    quantity: int
    unit_price: float

class CheckoutData(BaseModel):
    items: List[CheckoutItem] = Field(default_factory=list)
    confirmed: bool = False
    total_amount: float = 0.0
