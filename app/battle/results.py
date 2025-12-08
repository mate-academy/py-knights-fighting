def get_battle_results(*args, **kwargs) -> dict:
    result = {}
    for fighter in args:
        result[fighter["name"]] = fighter["hp"]
    return result
