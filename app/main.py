from app.battle_preparation.knights import Knight

from app.battle_progress.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = [
        Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        )
        for knight in knights_config.values()
    ]

    for knight in knights:
        knight.apply_changes()

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    Battle.fight(lancelot, mordred)
    Battle.fight(arthur, red_knight)

    return Battle.battle_result(knights)
