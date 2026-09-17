def generate_boost_plan(business_name: str, goal: str) -> dict:
    return {
        "business_name": business_name,
        "goal": goal,
        "next_steps": [
            "Define target customers",
            "Create weekly content plan",
            "Track leads and conversion metrics",
        ],
    }
