from app.knights import KNIGHTS

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


print(battle({"lancelot": KNIGHTS["lancelot"],
              "arthur": KNIGHTS["arthur"],
              "mordred": KNIGHTS["mordred"],
              "red_knight": KNIGHTS["red_knight"]}))
