def result_of_battle(knights: dict) -> dict:
    return {value.name: value.hp for value in knights.values()}
