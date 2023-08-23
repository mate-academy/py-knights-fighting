from My_knights import Knight
from data import persons


def fight(first: dict, second: dict) -> None:
    first["hp"] -= second["power"] - first["protection"]
    second["hp"] -= first["power"] - second["protection"]


def battle_function(prepared_heroes: dict) -> dict:
    fight(prepared_heroes["lancelot"], prepared_heroes["mordred"])
    fight(prepared_heroes["arthur"], prepared_heroes["red_knight"])
    for knight in prepared_heroes.values():
        if knight["hp"] <= 0:
            knight["hp"] = 0
    return {
        knight["name"]: knight["hp"]
        for knight in prepared_heroes.values()
    }


def battle(people: dict) -> dict:
    hero = Knight(people).preparing()
    return battle_function(hero)


print(battle(persons))
