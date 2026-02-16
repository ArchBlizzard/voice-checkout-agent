
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from app.schemas.call import TranscriptSegment, AnalysisResult, CheckoutData

class AnalyzerEngine(ABC):
    @abstractmethod
    def extract_from_transcripts(self, transcripts: List[TranscriptSegment], analyzers: List[Dict[str, Any]]) -> List[AnalysisResult]:
        pass

    @abstractmethod
    def generate_summary(self, transcripts: List[TranscriptSegment]) -> str:
        pass

    @abstractmethod
    def detect_checkout_intent(self, transcripts: List[TranscriptSegment]) -> Optional[CheckoutData]:
        pass
