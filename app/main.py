from app.knights.knights_config import KNIGHTS
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight.prepare_knight("lancelot", knights_config)
    print("---------------------------------------------------")
    arthur = Knight.prepare_knight("arthur", knights_config)
    print("---------------------------------------------------")
    mordred = Knight.prepare_knight("mordred", knights_config)
    print("---------------------------------------------------")
    red_knight = Knight.prepare_knight("red_knight", knights_config)
    print("---------------------------------------------------")

    # # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hit(mordred)
    mordred.hit(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.hit(red_knight)
    red_knight.hit(arthur)

    # Return battle results:
    return (
        {
            lancelot.name : lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp
        }
    )


print(battle(KNIGHTS))
