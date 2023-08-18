from My_knights import Knight
from data import persons


class Battle:
    @staticmethod
    def battle_function(prepared_heroes: dict) -> dict:
        value = prepared_heroes
        value["lancelot"]["hp"] -=\
            value["mordred"]["power"] - value["lancelot"]["protection"]
        value["mordred"]["hp"] -=\
            value["lancelot"]["power"] - value["mordred"]["protection"]

        if value["lancelot"]["hp"] <= 0:
            value["lancelot"]["hp"] = 0

        if value["mordred"]["hp"] <= 0:
            value["mordred"]["hp"] = 0
        value["arthur"]["hp"] -=\
            value["red_knight"]["power"] - value["arthur"]["protection"]
        value["red_knight"]["hp"] -=\
            value["arthur"]["power"] - value["red_knight"]["protection"]

        if value["arthur"]["hp"] <= 0:
            value["arthur"]["hp"] = 0

        if value["red_knight"]["hp"] <= 0:
            value["red_knight"]["hp"] = 0

        return {
            "Lancelot": value["lancelot"]["hp"],
            "Arthur": value["arthur"]["hp"],
            "Mordred": value["mordred"]["hp"],
            "Red Knight": value["red_knight"]["hp"]}


def battle(people: dict) -> dict:
    hero = Knight.preparing(people)
    return Battle.battle_function(hero)


print(battle(persons))
