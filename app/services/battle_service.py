from app.models.knight import Knight
from app.services.knight_factory import create_knight


def battle(knights_config: dict) -> dict:
    lancelot = create_knight(knights_config["lancelot"])
    arthur = create_knight(knights_config["arthur"])
    mordred = create_knight(knights_config["mordred"])
    red_knight = create_knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        "Lancelot": lancelot.hp,
        "Arthur": arthur.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp,
    }


def fight(knight1: Knight, knight2: Knight) -> None:
    damage1 = max(0, knight1.power - knight2.protection)
    damage2 = max(0, knight2.power - knight1.protection)

    knight2.hp = max(0, knight2.hp - damage1)
    knight1.hp = max(0, knight1.hp - damage2)
