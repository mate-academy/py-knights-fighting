from app.knights.battle_preparations import Knight
from app.actions.battle_round import battle_round


def battle(knights_config: dict) -> dict:

    knights = {
        knight["name"]: Knight(knight).apply_potion(knight)
        for index, knight in knights_config.items()
    }

    round_result = battle_round(knights)

    for name, knight in round_result.items():
        if knight.hp <= 0:
            knight.hp = 0

    return {knight.name: knight.hp for name, knight in round_result.items()}
