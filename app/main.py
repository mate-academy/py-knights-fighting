from app.knights.knights_info import KNIGHTS
from app.knights.reformatting_info import making_knight


def battle(knights_config: dict) -> dict:
    # Reformatting info about the Knights

    knights = {
        name: making_knight(knight)
        for name, knight in knights_config.items()
    }

# BATTLE------------------------------------------------

    # 1 Lancelot vs Mordred:

    knights["lancelot"].fight(knights["mordred"])

    # 2 Arthur vs Red Knight:

    knights["arthur"].fight(knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


print(battle(KNIGHTS))
