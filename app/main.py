from app.source import KNIGHTS
from app.combatant import Combatant
from app.duel import duel


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    lancelot = Combatant(knights_config["lancelot"])
    arthur = Combatant(knights_config["arthur"])
    mordred = Combatant(knights_config["mordred"])
    red_knight = Combatant(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    duel(lancelot, mordred)
    
    # 2 Arthur vs Red Knight:
    duel(arthur, red_knight)

    # Return battle results:

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
