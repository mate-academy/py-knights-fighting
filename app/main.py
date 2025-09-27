from app.knights.lancelot import lancelot
from app.knights.arthur import arthur
from app.knights.mordred import mordred
from app.knights.red_knight import red_knight
from app.preparing_to_fight.putting_on import putting_on
from app.battle.fight import fight


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
