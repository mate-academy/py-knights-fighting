import app.preparing.initialize as init
from app.preparing.knight import Knight


def battle(team: dict) -> dict:
    team = init.initialize(team)
    pairs = [
        ("Lancelot", "Mordred"),
        ("Arthur", "Red Knight"),
    ]
    for first, second in pairs:
        Knight.fight(team[first], team[second])
    return {
        "Lancelot": team["Lancelot"].hp,
        "Arthur": team["Arthur"].hp,
        "Mordred": team["Mordred"].hp,
        "Red Knight": team["Red Knight"].hp
    }
