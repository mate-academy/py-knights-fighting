from app.knights_battle.knight import Knight
from app.knights_battle.battle import battle_between_two
from app.knights_battle.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    ready_for_battle = {}
    for key in knights_config:
        knight = Knight(
            name=knights_config[key]["name"],
            power=knights_config[key]["power"],
            hp=knights_config[key]["hp"],
            weapon=knights_config[key]["weapon"],
            armour=knights_config[key]["armour"],
            potion=knights_config[key]["potion"],
        )
        ready_for_battle[knights_config[key]["name"]] = knight

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    battle_between_two(
        ready_for_battle["Lancelot"],
        ready_for_battle["Mordred"]
    )

    # 2 Arthur vs Red Knight:
    battle_between_two(
        ready_for_battle["Arthur"],
        ready_for_battle["Red Knight"]
    )

    # Return battle results:
    return {
        "Lancelot": ready_for_battle["Lancelot"].hp,
        "Arthur": ready_for_battle["Arthur"].hp,
        "Mordred": ready_for_battle["Mordred"].hp,
        "Red Knight": ready_for_battle["Red Knight"].hp
    }


print(battle(KNIGHTS))
