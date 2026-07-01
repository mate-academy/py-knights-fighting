def result(knights: list[dict]) -> dict:
    return {knight["name"]: knight["hp"] for knight in knights}
