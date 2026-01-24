from typing import Dict

from app.models.knight import Knight


def prepare_knight(config: Dict) -> Dict[str, int]:
    knight = Knight.from_config(config)
    return knight.final_stats()
