from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.config import settings
from app.payments.model import Payment
from app.callbacks.model import PaymentCallback

class CallbackService:
    
    def process_callback(self, body: dict, token: str):
        db: Session = SessionLocal()

        # 1. Verify callback signature/token
        if token != settings.XENDIT_CALLBACK_TOKEN:
            raise HTTPException(status_code=401, detail="Invalid callback token")

        event = body.get("event")
        invoice_id = body.get("id")
        status = body.get("status")

        # 2. Find payment by invoice ID
        payment = db.query(Payment).filter_by(
            xendit_invoice_id=invoice_id
        ).first()

        if not payment:
            raise HTTPException(404, "Payment not found")

        # 3. Idempotency
        if payment.callback_processed_at:
            return {"message": "already processed"}

        # 4. Save callback log
        callback_log = PaymentCallback(
            payment_id=payment.id,
            event=event,
            payload=body
        )
        db.add(callback_log)

        # 5. Update payment status
        if event == "invoice.paid":
            payment.status = "PAID"
        elif event == "invoice.expired":
            payment.status = "EXPIRED"
        elif event == "invoice.failed":
            payment.status = "FAILED"
        else:
            payment.status = status

        payment.callback_processed_at = datetime.utcnow()

        db.commit()
        db.refresh(payment)

        return {"message": "callback processed", "status": payment.status}
