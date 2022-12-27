from app.model.battle import Battle
from app.model.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight().parse_knight_stats("lancelot", knights_config)
    arthur = Knight().parse_knight_stats("arthur", knights_config)
    mordred = Knight().parse_knight_stats("mordred", knights_config)
    red_knight = Knight().parse_knight_stats("red_knight", knights_config)

    # lancelot
    lancelot.calculate_final_stats()
    arthur.calculate_final_stats()
    mordred.calculate_final_stats()
    red_knight.calculate_final_stats()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle(lancelot, mordred).fight()

    # 2 Arthur vs Red Knight:
    Battle(arthur, red_knight).fight()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
