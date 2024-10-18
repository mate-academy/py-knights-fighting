def return_battles_results(knights: list) -> dict:
    results = {}
    for knight in knights:
        if knight["hp"] <= 0:
            results[knight["name"]] = 0
        else:
            results[knight["name"]] = knight["hp"]

    return results
