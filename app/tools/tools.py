import json

from app.people.knight import Knight


def knights_from_dict(data: dict) -> dict:
    return {
        name: Knight.create_from_dict(knight)
        for name, knight in data.items()
    }


def dict_knights_from_file(filename: str) -> dict:
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {}

    return data


def knights_from_file(filename: str) -> dict[str, Knight]:
    data = dict_knights_from_file(filename)
    return knights_from_dict(data)


def prepare_all_to_fights(knights: dict[str, Knight]) -> dict:
    for knight in knights.values():
        knight.prepare_to_fight()
