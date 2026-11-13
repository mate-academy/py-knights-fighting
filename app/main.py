import app.preparing.initialize as init
from app.preparing.knight import Knight


def battle(team: dict) -> dict:
    team = init.initialize(team)
    Knight.fight(team["Lancelot"], team["Mordred"])
    Knight.fight(team["Arthur"], team["Red Knight"])
    return {
        "Lancelot": team["Lancelot"].hp,
        "Arthur": team["Arthur"].hp,
        "Mordred": team["Mordred"].hp,
        "Red Knight": team["Red Knight"].hp
    }
