from app.knights_points.knights_points import knight_points
from app.knights_points.fight import fight
from app.knights_points.knights import KNIGHTS


def battle(knights: dict) -> dict:
    lancelot = knight_points(knights["lancelot"])
    arthur = knight_points(knights["arthur"])
    mordred = knight_points(knights["mordred"])
    red_knight = knight_points(knights["red_knight"])

    # # 1 Lancelot vs Mordred:
    lancelot, mordred = fight(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    arthur, red_knight = fight(arthur, red_knight)
    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
