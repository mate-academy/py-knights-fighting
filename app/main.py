from app.knights.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, config in knights_config.items():
        knights[key] = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    battle_results = {}

    # 1 Lancelot vs Mordred
    lancelot_vs_mordred = Battle(
        lancelot.prepare_battle(), mordred.prepare_battle()
    )
    battle_results.update(lancelot_vs_mordred.start_battle())

    # 2 Arthur vs Red Knight
    arthur_vs_red_knight = Battle(
        arthur.prepare_battle(), red_knight.prepare_battle()
    )
    battle_results.update(arthur_vs_red_knight.start_battle())

    return battle_results
