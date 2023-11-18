from app.config.data import all_knights_doc
from app.config.battle_1vs1 import battle_1vs1
from app.config.knights import Knights
from app.config.calculations import calculations


def battle(all_knights_doc: dict) -> dict:
    for characteristics in all_knights_doc.values():
        result = calculations(characteristics)
        Knights(
            characteristics["name"],
            characteristics["power"] + result["power"],
            characteristics["hp"] + result["hp"],
            result["protection"]
        )
    # who fight, variable name = knight name
    battle_1vs1("Lancelot", "Mordred")
    battle_1vs1("Arthur", "Red Knight")
    # Return battle results:
    return {knight.name: knight.hp for knight in Knights.persons.values()}


print(battle(all_knights_doc))
