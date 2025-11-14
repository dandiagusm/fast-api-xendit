from pydantic import BaseModel, Field
from typing import Optional

class XenditCallbackRequest(BaseModel):
    id: str = Field(..., example="inv-d7acb81d-6c45-4e20-a8f5-9bb1f75aa093")
    external_id: str = Field(..., example="ORDER-12345")
    status: str = Field(..., example="PAID")
    event: str = Field(..., example="invoice.paid")
    amount: Optional[int] = Field(None, example=50000)
    paid_at: Optional[str] = Field(None, example="2025-02-10T10:22:30.652Z")

    class Config:
        from_attributes = True
