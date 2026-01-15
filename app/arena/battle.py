from app.fighters.knight import Knight


def knights_preparation(knights: list[Knight]) -> list[Knight]:
    return [knight.preparing_for_battle() for knight in knights]


def start_battle(first_knight: Knight, second_knight: Knight) -> dict:
    first_knight.battle_with(second_knight)
    second_knight.battle_with(first_knight)

    first_knight.check_if_defeated()
    second_knight.check_if_defeated()

    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp
    }


def get_battle_results(battles: list[dict]) -> dict:
    battle_results = battles[0]
    for i in range(1, len(battles)):
        battle_results.update(battles[i])

    return battle_results
