from app.battle.battle_fight import fight
from app.battle.battle_prep import knight_stats_preparation
from app.knights.knights import KNIGHTS
from app.knights.knights_stats import Knight


def battle(knightsconfig: dict) -> dict:
    contestants = []
    for key, value in knightsconfig.items():
        value = Knight(value)
        knight_stats_preparation(value)
        contestants.append(value)

    fight(contestants[0], contestants[2])
    fight(contestants[1], contestants[3])

    return {
        contestants[0].name: contestants[0].hp,
        contestants[1].name: contestants[1].hp,
        contestants[2].name: contestants[2].hp,
        contestants[3].name: contestants[3].hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
