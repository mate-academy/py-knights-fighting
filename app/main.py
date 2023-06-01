from app.knights_person.knight import Knight
from app.battle.battle_service import Battle
from app.data.data_service import data


def battle(knights_config: dict) -> dict:
    knights_list = []
    for knight in knights_config.values():
        person = Knight(knight["name"], knight["hp"], knight["power"])
        person.set_protection(knight["armour"])
        person.set_power(knight["weapon"])
        person.set_potion(knight["potion"])
        knights_list.append(person)

    Battle.fight(knights_list[0], knights_list[2])
    Battle.fight(knights_list[2], knights_list[0])

    Battle.fight(knights_list[1], knights_list[3])
    Battle.fight(knights_list[3], knights_list[1])

    return Battle.results(knights_list)


knights = data()
print(battle(knights))
