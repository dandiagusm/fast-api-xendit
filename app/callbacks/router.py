from fastapi import APIRouter, Request, Header
from app.callbacks.service import CallbackService
from app.callbacks.schema import XenditCallbackRequest

router = APIRouter()
service = CallbackService()

@router.post(
    "/xendit",
    summary="Callback dari Xendit",
    description="Endpoint untuk menerima event dari Xendit seperti invoice.paid, invoice.expired, invoice.failed.",
    response_description="Hasil pemrosesan callback."
)
async def xendit_callback(
    payload: XenditCallbackRequest,
    x_callback_token: str = Header(None, description="Callback token dari Xendit (X-CALLBACK-TOKEN)")
):
    # payload = await request.json()  # sudah otomatis oleh FastAPI
    return service.process_callback(payload.dict(), x_callback_token)
