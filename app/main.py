from typing import Dict
from app.knight.knight import Knight


def battle(knights_config: Dict) -> Dict:
    knights = {
        name: Knight(**config)
        for name, config in knights_config.items()
    }

    knights["Lancelot"].duel(knights["Mordred"])
    knights["Arthur"].duel(knights["Red_knight"])

    return {name: knight.hp for name, knight in knights.items()}
