from app.battle.battle import BattleStats
from app.knights.knight import Knight


def battle(knightsconfig: dict) -> dict:
    knights = [
        Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        )
        for knight in knightsconfig.values()
    ]
    for knight in knights:
        knight.apply_factors()

    BattleStats.battle(knights[0], knights[2])
    BattleStats.battle(knights[1], knights[3])
    return BattleStats.result_message(knights)
