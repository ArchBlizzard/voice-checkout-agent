
import asyncio
from app.db.database import get_db, SessionLocal
from app.db import models as db_models
from app.utils.pdf_generator import InvoiceGenerator
from app.schemas.call import CheckoutData
from loguru import logger

class BackgroundWorker:
    def process_post_call_tasks(self, call_id: str, checkout_data: CheckoutData):
        logger.info(f"Starting background task for call_id: {call_id}")
        
        db = SessionLocal()
        try:
            # Simulate consumption
            if checkout_data.confirmed:
                pdf_items = []
                
                for item in checkout_data.items:
                    # Update or Create Inventory Item
                    inv_item = db.query(db_models.Inventory).filter(db_models.Inventory.product_name == item.product_name).first()
                    if not inv_item:
                         inv_item = db_models.Inventory(product_name=item.product_name, stock_count=50, price=item.unit_price)
                         db.add(inv_item)
                         db.commit()
                    
                    inv_item.stock_count -= item.quantity
                    db.add(inv_item)
                    
                    pdf_items.append({
                        "name": item.product_name,
                        "price": item.unit_price,
                        "qty": item.quantity
                    })
                
                # 2. Generate Invoice
                generator = InvoiceGenerator()
                invoice_path = generator.generate_invoice(
                    call_id=call_id,
                    amount=checkout_data.total_amount,
                    items=pdf_items
                )
                
                # 3. Store Invoice Record
                new_invoice = db_models.Invoice(
                    call_id=call_id,
                    amount=checkout_data.total_amount,
                    pdf_path=invoice_path
                )
                db.add(new_invoice)
                db.commit()
                logger.info(f"Invoice generated at {invoice_path} with {len(pdf_items)} items")
            
        except Exception as e:
            logger.error(f"Background task failed: {e}")
            db.rollback()
        finally:
            db.close()

background_worker = BackgroundWorker()
