from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"msg": "User route works"}
