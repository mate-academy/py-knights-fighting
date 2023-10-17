from app.arenas.camelot import Camelot
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:

    battles_results = {}

    battle_arena = Camelot()
    [Knight(name=knight["name"],
            hp=knight["hp"],
            power=knight["power"],
            armour=knight["armour"],
            weapon=knight["weapon"],
            potion=knight["potion"])
        for knight in knights_config.values()]

    first_battle_result = battle_arena.knight_battle(
        Knight.knights_for_battle["Lancelot"].prep_for_battle(),
        Knight.knights_for_battle["Mordred"].prep_for_battle()
    )

    second_battle_result = battle_arena.knight_battle(
        Knight.knights_for_battle["Arthur"].prep_for_battle(),
        Knight.knights_for_battle["Red Knight"].prep_for_battle()
    )

    battles_results.update(first_battle_result)

    battles_results.update(second_battle_result)

    return battles_results
