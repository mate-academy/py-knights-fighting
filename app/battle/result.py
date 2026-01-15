def result_of_battle(fighters: dict) -> dict:

    return {knight.name: knight.hp for knight in fighters.values()}
