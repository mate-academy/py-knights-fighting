from app.knights.knight import Knight
from app.knights.knights_config import KNIGHTS
from app.battle.battle import Battle


def battle(knights: dict) -> dict:

    dict_of_knights = {
        key: Knight(
            name=value.get("name"),
            power=value.get("power"),
            hp=value.get("hp"),
            armour=value.get("armour"),
            weapon=value.get("weapon"),
            potion=value.get("potion"),
        )
        for key, value in knights.items()
    }

    battle_results = {}

    lancelot = dict_of_knights["lancelot"]
    arthur = dict_of_knights["arthur"]
    mordred = dict_of_knights["mordred"]
    red_knight = dict_of_knights["red_knight"]

    # 1 Lancelot vs Mordred:
    lancelot_vs_mordred = Battle(lancelot.prepare_battle(),
                                 mordred.prepare_battle())
    first_battle = lancelot_vs_mordred.start_battle()
    battle_results.update(first_battle)

    # 2 Arthur vs Red Knight:
    arthur_vs_red_knight = Battle(arthur.prepare_battle(),
                                  red_knight.prepare_battle())
    second_battle = arthur_vs_red_knight.start_battle()
    battle_results.update(second_battle)

    return battle_results


print(battle(KNIGHTS))
