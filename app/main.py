from app.knights.red_knight import red_knight
from app.knights.mordred import mordred
from app.knights.arthur import arthur
from app.knights.lancelot import lancelot

from app.actions.preparations import prepare
from app.actions.fight import fight


def battle(knightsconfig: dict) -> dict:
    lancelot = knightsconfig["lancelot"]
    prepare(lancelot)

    arthur = knightsconfig["arthur"]
    prepare(arthur)

    mordred = knightsconfig["mordred"]
    prepare(mordred)

    red_knight = knightsconfig["red_knight"]
    prepare(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle({"lancelot": lancelot,
              "arthur": arthur,
              "mordred": mordred,
              "red_knight": red_knight}))
