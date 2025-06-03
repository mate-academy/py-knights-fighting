from app.battle.battle_fight import fight
from app.battle.battle_prep import knight_stats_preparation
from app.knights.knights import KNIGHTS
from app.knights.knights_stats import Knight


def battle(knightsconfig: dict) -> dict:

    contestants = {}

    for key, value in knightsconfig.items():
        value = Knight(value)
        knight_stats_preparation(value)
        contestants[value.name] = value

    fight(contestants["Lancelot"], contestants["Mordred"])
    fight(contestants["Arthur"], contestants["Red Knight"])

    return {val.name : val.hp for val in contestants.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
