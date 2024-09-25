from app.knights.param import Knight
from app.battle.knights_battle import knights_battle


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    lancelot = Knight(
        knights_config["lancelot"]["name"],
        knights_config["lancelot"]["hp"],
        knights_config["lancelot"]["power"]
    )
    lancelot.calculate_param(knights_config["lancelot"])

    arthur = Knight(
        knights_config["arthur"]["name"],
        knights_config["arthur"]["hp"],
        knights_config["arthur"]["power"]
    )
    arthur.calculate_param(knights_config["arthur"])

    mordred = Knight(
        knights_config["mordred"]["name"],
        knights_config["mordred"]["hp"],
        knights_config["mordred"]["power"]
    )
    mordred.calculate_param(knights_config["mordred"])

    red_knight = Knight(
        knights_config["red_knight"]["name"],
        knights_config["red_knight"]["hp"],
        knights_config["red_knight"]["power"]
    )
    red_knight.calculate_param(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights_battle(lancelot, mordred)
    # 2 Arthur vs Red_Knight:
    knights_battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
