
from fastapi import BackgroundTasks
from app.schemas.call import CallPayload, AnalysisResult, CheckoutData
from app.services.analyzer_engine import AnalyzerEngine
from app.services.extraction_service import ExtractionService
from app.workers.background_tasks import background_worker
from app.core.logging_config import logger

class CallProcessor:
    def __init__(self, analyzer_engine: AnalyzerEngine):
        self.analyzer_engine = analyzer_engine

    async def process_call(self, payload: CallPayload, background_tasks: BackgroundTasks) -> CallPayload:
        logger.info(f"Processing call {payload.call_id}")
        
        # 1. Run Analysis Extraction
        new_analysis_results = self.analyzer_engine.extract_from_transcripts(
            transcripts=payload.transcripts,
            analyzers=payload.analyzers
        )
        
        # Merge new results with existing
        payload.analysis_results.extend(new_analysis_results)
        
        # 2. Generate Summary
        if not payload.summary:
            payload.summary = self.analyzer_engine.generate_summary(payload.transcripts)
            
        # 3. Check for Checkout / Action Items
        checkout_data = self.analyzer_engine.detect_checkout_intent(payload.transcripts)
        
        # 4. Enqueue Background Tasks if checkout detected
        if checkout_data and checkout_data.confirmed:
            logger.info("Checkout intent detected. Enqueueing background tasks.")
            background_tasks.add_task(
                background_worker.process_post_call_tasks, 
                call_id=payload.call_id, 
                checkout_data=checkout_data
            )
            
        return payload

# Dependency Injection Factory
def get_call_processor() -> CallProcessor:
    return CallProcessor(analyzer_engine=ExtractionService())
