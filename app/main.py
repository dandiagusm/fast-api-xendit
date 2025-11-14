from fastapi import FastAPI
from app.payments.router import router as payment_router
from app.callbacks.router import router as callback_router

app = FastAPI(title="Briliq Payment System")

# Routers
app.include_router(payment_router, prefix="/payments", tags=["Payments"])
app.include_router(callback_router, prefix="/callbacks", tags=["Callbacks"])

@app.get("/")
def health():
    return {"status": "ok", "service": "briliq-payment-system"}
