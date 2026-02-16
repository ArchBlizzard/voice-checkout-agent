
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.schemas.call import CallPayload
from app.services.call_processor import CallProcessor, get_call_processor
from app.core.logging_config import logger

router = APIRouter()

@router.post("/webhook", response_model=CallPayload)
async def process_call_webhook(
    payload: CallPayload, 
    background_tasks: BackgroundTasks,
    processor: CallProcessor = Depends(get_call_processor)
):
    try:
        logger.info(f"Received webhook for call {payload.call_id}")
        
        updated_payload = await processor.process_call(payload, background_tasks)
        
        return updated_payload
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
