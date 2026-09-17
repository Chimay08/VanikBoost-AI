from fastapi import APIRouter
from backend.schemas.product import ProductCreate
from backend.services.product_service import create_product, get_products

router = APIRouter()


@router.post("/products")
def add_product(product: ProductCreate):
    result = create_product(product)

    return {
        "message": "Product created successfully",
        "product": result
    }


@router.get("/products")
def list_products():
    return get_products()
