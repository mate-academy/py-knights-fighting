from app.knight.knight import Knight


def output(knights: [Knight]) -> dict:
    result = {}
    for item in knights:
        name = getattr(item, "name")
        result[name] = item.hp

    return result
