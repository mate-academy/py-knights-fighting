from app.knights.lancelot import lancelot
from app.knights.arthur import arthur
from app.knights.mordred import mordred
from app.knights.red_knight import red_knight
from app.battle.preparation import Preparation
from app.battle.battle import battle_versus


KNIGHTS = {
    "lancelot": lancelot(),
    "arthur": arthur(),
    "mordred": mordred(),
    "red_knight": red_knight()
}


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Preparation(knightsconfig["lancelot"])

    # arthur
    arthur = Preparation(knightsconfig["arthur"])

    # mordred
    mordred = Preparation(knightsconfig["mordred"])

    # red_knight
    red_knight = Preparation(knightsconfig["red_knight"])

    knights = [lancelot, arthur, mordred, red_knight]
    # -------------------------------------------------------------------------------
    # BATTLE:
    battle_versus(lancelot.knight, mordred.knight)

    # 2 Arthur vs Red Knight:
    battle_versus(arthur.knight, red_knight.knight)

    # Return battle results:
    return {
        knight.knight["name"]: knight.knight["hp"] for knight in knights
    }


print(battle(KNIGHTS))
