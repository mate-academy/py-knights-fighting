from app.config.config_knights import KNIGHTS
from app.knights.knights_class import Knights
from app.knights.prepare_for_battle import prepare_knight_for_battle


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # Creation of knights:
    lancelot = Knights(**knights_config["lancelot"])
    arthur = Knights(**knights_config["arthur"])
    mordred = Knights(**knights_config["mordred"])
    red_knight = Knights(**knights_config["red_knight"])

    # BATTLE PREPARATIONS:
    prepare_knight_for_battle(lancelot,
                              arthur,
                              mordred,
                              red_knight)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # Return battle results:
    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}


print(battle(KNIGHTS))
