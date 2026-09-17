import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.routes.health import router as health_router
from backend.routes.products import router as products_router
from backend.routes.sale import router as sales_router

app = FastAPI()

app.include_router(health_router)
app.include_router(products_router)
app.include_router(sales_router)


@app.get("/")
def home():
    return {"message": "VanikBoost API is running"}


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
