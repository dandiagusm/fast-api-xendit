from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    external_id = Column(String, nullable=False)
    xendit_invoice_id = Column(String, unique=True)
    amount = Column(Float, nullable=False)
    status = Column(String, default="PENDING")
    invoice_url = Column(String)
    expiry_date = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        onupdate=func.now()
    )
