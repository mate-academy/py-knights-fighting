def battle_result(knights_config: dict) -> dict:
    result = {}
    for knight in knights_config.keys():
        result.update({knights_config[knight]["name"]:
                       knights_config[knight]["hp"]})
    return result
