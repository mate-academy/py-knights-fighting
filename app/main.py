from app.knights.models import Knight
from app.knights.config import KNIGHTS


def apply_damage(attacker: Knight, defender: Knight) -> None:
    damage = attacker.power - defender.protection
    defender.take_damage(damage)


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    apply_damage(knights["lancelot"], knights["mordred"])
    apply_damage(knights["mordred"], knights["lancelot"])

    apply_damage(knights["arthur"], knights["red_knight"])
    apply_damage(knights["red_knight"], knights["arthur"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
