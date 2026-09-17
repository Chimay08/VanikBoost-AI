from fastapi import APIRouter

router = APIRouter(tags=["sales"])


@router.post("/sales")
def create_sale():
    return {"message": "Sales endpoint is ready"}
