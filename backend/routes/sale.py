from fastapi import APIRouter

router = APIRouter(prefix="/sales", tags=["sales"])


@router.post("")
def create_sale():
    return {"message": "Sales endpoint is ready"}
