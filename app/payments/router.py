from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.payments.schema import CreatePaymentRequest, PaymentResponse
from app.payments.service import PaymentService

router = APIRouter()
service = PaymentService()

@router.post("/", response_model=PaymentResponse)
def create_payment(payload: CreatePaymentRequest, db: Session = Depends(get_db)):
    return service.create_payment(payload, db)
