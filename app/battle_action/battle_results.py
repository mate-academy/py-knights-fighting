def results(result_1: list, result_2: list) -> dict:
    return {
        result_1[0]["name"]: result_1[0]["hp"],
        result_2[0]["name"]: result_2[0]["hp"],
        result_1[1]["name"]: result_1[1]["hp"],
        result_2[1]["name"]: result_2[1]["hp"],
    }
