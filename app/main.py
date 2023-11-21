from app.config.data import all_knights_doc
from app.config.battle_1vs1 import battle_1vs1
from app.config.knight import Knight


def battle(all_knights_doc: dict) -> dict:
    for characteristics in all_knights_doc.values():
        person = Knight(
            characteristics["name"],
            characteristics["power"],
            characteristics["hp"]
        )
        person.calculations(characteristics)
    # who fight, variable name = knight name
    battle_1vs1("Lancelot", "Mordred")
    battle_1vs1("Arthur", "Red Knight")
    # Return battle results:
    return {knight.name: knight.hp for knight in Knight.persons.values()}


print(battle(all_knights_doc))
