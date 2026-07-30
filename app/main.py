from app.models.knight import Knight
from app.services.battle import conduct_battle


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(
            name=stats["name"],
            power=stats["power"],
            hp=stats["hp"],
            armour=stats["armour"],
            weapon=stats["weapon"],
            potion=stats["potion"],
        )
        for name, stats in knights_config.items()
    }

    # Battles
    conduct_battle(knights["lancelot"], knights["mordred"])
    conduct_battle(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
