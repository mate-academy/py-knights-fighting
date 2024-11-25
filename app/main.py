from app.battle.creating_knights import creating_knight
from app.battle.fight import fight
from app.knights import knights_config


def battle(knights_config: dict = knights_config.KNIGHTS) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = creating_knight("lancelot", knights_config)
    arthur = creating_knight("arthur", knights_config)
    mordred = creating_knight("mordred", knights_config)
    red_knight = creating_knight("red_knight", knights_config)
    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle())
