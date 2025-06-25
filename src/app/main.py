from fastapi import FastAPI

from app.api.api_v1.api import api_router

app = FastAPI(title="Virtual Wallet")

app.include_router(api_router, prefix="/test")

@app.get("/")
def read_root():
    return {"msg": "Virtual Wallet API"}

