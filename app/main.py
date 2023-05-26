from app.knights.red_knight import red_knight
from app.knights.mordred import mordred
from app.knights.arthur import arthur
from app.knights.lancelot import lancelot

from app.actions.preparations import prepare
from app.actions.fight import fight


def battle(knightsconfig: dict) -> dict:

    knights = [knightsconfig["lancelot"],
               knightsconfig["arthur"],
               knightsconfig["mordred"],
               knightsconfig["red_knight"]]

    for knight in knights:
        prepare(knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(knights[0], knights[2])

    # 2 Arthur vs Red Knight:
    fight(knights[1], knights[3])

    # Return battle results:
    return {
        knight["name"]: knight["hp"]
        for knight in knights
    }


print(battle({"lancelot": lancelot,
              "arthur": arthur,
              "mordred": mordred,
              "red_knight": red_knight}))
