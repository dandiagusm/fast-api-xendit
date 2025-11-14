from fastapi import FastAPI
from app.payments.router import router as payment_router

app = FastAPI()

app.include_router(payment_router, prefix="/payments", tags=["Payments"])

@app.get("/")
def health_check():
    return {"status": "ok"}
