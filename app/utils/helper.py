from typing import Dict
from app.models.knight import Knight


def build_knights(config: Dict[str, dict]) -> Dict[str, Knight]:
    return {key: Knight(data) for key, data in config.items()}
