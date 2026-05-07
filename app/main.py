from app.config import KNIGHTS
from app.battle.preparations import battle_preparation
from app.battle.fight import fighting, battle_results


BATTLE_PARTNERS = (
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
)


def battle(knights_config: dict) -> dict:
    battle_prepared_knights = {
        knight: battle_preparation(knight_data)
        for knight, knight_data in knights_config.items()
    }

    for first_partner, second_partner in BATTLE_PARTNERS:
        fighting(
            battle_prepared_knights[first_partner],
            battle_prepared_knights[second_partner],
        )

    return battle_results(battle_prepared_knights.values())


if __name__ == "__main__":
    print(battle(KNIGHTS))
