from sqlalchemy.orm import Session
from app.payments.model import Payment
from app.utils.xendit_client import XenditClient

class PaymentService:

    def __init__(self):
        self.xendit = XenditClient()

    def create_payment(self, payload, db: Session):
        # 1. Create invoice in Xendit
        invoice = self.xendit.create_invoice(
            external_id=payload.external_id,
            amount=payload.amount
        )

        # 2. Store payment in DB
        payment = Payment(
            user_id=payload.user_id,
            external_id=payload.external_id,
            xendit_invoice_id=invoice["id"],
            amount=payload.amount,
            status=invoice["status"],
            invoice_url=invoice["invoice_url"],
            expiry_date=invoice["expiry_date"],
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment
