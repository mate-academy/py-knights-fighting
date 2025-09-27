from knights.lancelot import lancelot
from knights.arthur import arthur
from knights.mordred import mordred
from knights.red_knight import red_knight
from preparing_to_fight.putting_on import putting_on
from battle.fight import fight


def battle() -> dict:
    knights = [lancelot, arthur, mordred, red_knight]
    # BATTLE PREPARATIONS:
    # apply armour weapon and potion if exist
    for knight in knights:
        putting_on(knight)
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred and also check if someone fell in battle:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight and also check if someone fell in battle:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
