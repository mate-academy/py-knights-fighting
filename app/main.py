from app.preparing.initialize import initialize
from app.preparing.knight import Knight


def battle(team: dict) -> dict:
    team = initialize(team)
    pairs = [
        ("Lancelot", "Mordred"),
        ("Arthur", "Red Knight"),
    ]
    for first, second in pairs:
        Knight.fight(team[first], team[second])
    return {
        knight.name: knight.hp for knight in team.values()
    }
