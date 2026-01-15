from typing import Dict

from app.knights_config import knights_config
from app.knight import Knight


def apply_effects(knight: Knight) -> None:
    knight.apply_effects()


def conduct_battle(knight1: Knight, knight2: Knight) -> None:
    damage1 = max(0, knight2.power - knight1.protection)
    damage2 = max(0, knight1.power - knight2.protection)

    knight1.hp = max(0, knight1.hp - damage1)
    knight2.hp = max(0, knight2.hp - damage2)


def battle(knight_config: Dict[str, dict]) -> Dict[str, int]:
    knights = {name: Knight(**data) for name, data in knight_config.items()}

    for knight in knights.values():
        apply_effects(knight)

    for knight_name1, knight_name2 in [
        ("lancelot", "mordred"), ("arthur", "red_knight")
    ]:
        conduct_battle(knights[knight_name1], knights[knight_name2])

    return {knight.name: knight.hp
            for name, knight in knights.items()}


def main() -> None:
    battle_result = battle(knights_config)
    print(battle_result)


if __name__ == "__main__":
    main()
