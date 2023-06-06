from app.knights_person.knight import Knight
from app.battle.battle_service import Battle


def battle(knights_config: dict) -> dict:
    knights = []
    for knight in knights_config.values():
        person = Knight(knight["name"], knight["hp"], knight["power"])
        person.set_protection(knight["armour"])
        person.set_power(knight["weapon"])
        person.set_potion(knight["potion"])
        knights.append(person)

    for i in range(len(knights) // 2):
        Battle.fight(knights[i], knights[i + 2])

    return Battle.results(knights)
