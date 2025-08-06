from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Virtual Wallet API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Welcome to Virtual Wallet API"}