from backend.services.ai_service import generate_boost_plan


def create_boost_plan(business_name: str, goal: str) -> dict:
    return generate_boost_plan(business_name=business_name, goal=goal)
