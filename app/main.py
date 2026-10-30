from app.models.knight import Knight
from app.services.fight import fight
from app.knights import KNIGHTS


def battle(
    first_knight_key: str,
    second_knight_key: str,
) -> dict[str, int]:
    first_knight = Knight.from_config(
        KNIGHTS[first_knight_key],
    )
    second_knight = Knight.from_config(
        KNIGHTS[second_knight_key],
    )

    first_knight.prepare_for_battle()
    second_knight.prepare_for_battle()

    fight(first_knight, second_knight)

    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp,
    }
