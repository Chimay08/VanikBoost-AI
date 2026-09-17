from fastapi import APIRouter

from backend.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse)
def health_check():
    return HealthResponse(status="ok", service="vanikboost-ai-api")
