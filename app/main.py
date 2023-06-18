from app.primary_received_info import KNIGHTS
from app.class_and_their_description import KnightCreator


def battle(base_knights: dict) -> dict:
    lancelot = KnightCreator(base_knights.get("lancelot"))
    upgrade_lancelot = lancelot.upgrading_knight(base_knights.get("lancelot"))

    arthur = KnightCreator(base_knights.get("arthur"))
    upgrade_arthur = arthur.upgrading_knight(base_knights.get("arthur"))

    mordred = KnightCreator(base_knights.get("mordred"))
    upgrade_mordred = mordred.upgrading_knight(base_knights.get("mordred"))

    red_knight = KnightCreator(base_knights.get("red_knight"))
    upgrade_red_knight = red_knight.upgrading_knight(
        base_knights.get("red_knight")
    )

    first_duel = KnightCreator.duel(upgrade_lancelot, upgrade_mordred)
    second_duel = KnightCreator.duel(upgrade_arthur, upgrade_red_knight)
    first_duel.update(second_duel)

    return first_duel


print(battle(KNIGHTS))
