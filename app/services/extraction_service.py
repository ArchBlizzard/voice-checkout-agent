
from typing import List, Dict, Any, Optional
from app.services.analyzer_engine import AnalyzerEngine
from app.schemas.call import TranscriptSegment, AnalysisResult, CheckoutData, Analyzer, CheckoutItem
import re

class ExtractionService(AnalyzerEngine):
    def extract_from_transcripts(self, transcripts: List[TranscriptSegment], analyzers: List[Analyzer]) -> List[AnalysisResult]:
        results = []
        full_text = " ".join([t.text for t in transcripts])
        
        for analyzer in analyzers:
            # Simulate extraction logic based on analyzer type
            extracted_data = {}
            confidence = 0.0

            if analyzer.type == "intent_recognition":
                extracted_data = {"intent": "purchase" if "buy" in full_text else "inquiry"}
                confidence = 0.95
            elif analyzer.type == "sentiment_analysis":
                extracted_data = {"sentiment": "positive" if "thank" in full_text else "neutral"}
                confidence = 0.88
            
            results.append(AnalysisResult(
                analyzer_id=analyzer.id,
                result=extracted_data,
                confidence_score=confidence
            ))
            
        return results

    def generate_summary(self, transcripts: List[TranscriptSegment]) -> str:
        # Simulate summarization
        return f"User interaction with {len(transcripts)} turns. Topic: General Inquiry/Purchase."

    def detect_checkout_intent(self, transcripts: List[TranscriptSegment]) -> Optional[CheckoutData]:
        full_text = " ".join([t.text for t in transcripts]).lower()
        
        # Simple simulated extraction for plumbing context
        checkout_data = CheckoutData()
        items = []

        # Logic to detect items in text (Mocking LLM extraction)
        if "p-trap" in full_text:
            items.append(CheckoutItem(product_name="P-Trap Replacement", quantity=1, unit_price=45.00))
        
        if "copper fittings" in full_text:
            # Try to find quantity for fittings
            qty = 1
            if "two" in full_text or "2 " in full_text: qty = 2
            elif "three" in full_text or "3 " in full_text: qty = 3
            items.append(CheckoutItem(product_name="1-inch Copper Fitting", quantity=qty, unit_price=8.50))

        if "valve" in full_text:
             items.append(CheckoutItem(product_name="Shutoff Valve", quantity=1, unit_price=25.00))

        if items:
            checkout_data.confirmed = True
            checkout_data.items = items
            checkout_data.total_amount = sum([i.quantity * i.unit_price for i in items])
            return checkout_data
            
        return None
