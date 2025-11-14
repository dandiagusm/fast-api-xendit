from pydantic import BaseModel

class CreatePaymentRequest(BaseModel):
    user_id: int
    amount: float
    external_id: str  # from Briliq-BE

class PaymentResponse(BaseModel):
    invoice_url: str
    xendit_invoice_id: str
    status: str

    class Config:
        orm_mode = True
