
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

class InvoiceGenerator:
    def generate_invoice(self, call_id: str, amount: float, items: list) -> str:
        output_dir = "generated_invoices"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        filename = f"{output_dir}/invoice_{call_id}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        
        c.drawString(100, 750, f"Invoice for Call ID: {call_id}")
        c.drawString(100, 730, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        y_position = 700
        c.drawString(100, y_position, "Items:")
        y_position -= 20
        
        for item in items:
            c.drawString(120, y_position, f"- {item['name']}: ${item['price']} x {item['qty']}")
            y_position -= 20
            
        c.drawString(100, y_position - 20, f"Total Amount: ${amount:.2f}")
        
        c.save()
        return filename
