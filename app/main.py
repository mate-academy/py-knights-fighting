from app.knights import Knight
from app.battle import fight


def battle(knightsconfig: dict) -> dict[str, dict[str, int]]:
    lancelot = Knight(knightsconfig["lancelot"])
    mordred = Knight(knightsconfig["mordred"])
    arthur = Knight(knightsconfig["arthur"])
    red_knight = Knight(knightsconfig["red_knight"])

    result1 = fight(lancelot, mordred)
    result2 = fight(arthur, red_knight)

    return {
        "Lancelot vs Mordred": result1,
        "Arthur vs Red Knight": result2,
    }
