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

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.knight["hp"] = battle_versus(lancelot.knight["hp"],
                                          mordred.knight["power"],
                                          lancelot.knight["protection"])

    mordred.knight["hp"] = battle_versus(mordred.knight["hp"],
                                         lancelot.knight["power"],
                                         mordred.knight["protection"])

    # 2 Arthur vs Red Knight:
    arthur.knight["hp"] = battle_versus(arthur.knight["hp"],
                                        red_knight.knight["power"],
                                        arthur.knight["protection"])

    red_knight.knight["hp"] = battle_versus(red_knight.knight["hp"],
                                            arthur.knight["power"],
                                            red_knight.knight["protection"])

    # Return battle results:
    return {
        lancelot.knight["name"]: lancelot.knight["hp"],
        arthur.knight["name"]: arthur.knight["hp"],
        mordred.knight["name"]: mordred.knight["hp"],
        red_knight.knight["name"]: red_knight.knight["hp"],
    }


print(battle(KNIGHTS))
