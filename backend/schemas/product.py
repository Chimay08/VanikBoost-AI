from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    category: str
    cost_price: float
    selling_price: float
    stock: int
