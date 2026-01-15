from app.knights_person.knight import Knight
from app.battle.battle_service import Battle


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, knight in knights_config.items():
        person = Knight(knight["name"], knight["hp"], knight["power"])
        person.set_protection(knight["armour"])
        person.set_power(knight["weapon"])
        person.set_potion(knight["potion"])
        knights[key] = person

    Battle.fight(knights.get("lancelot"), knights.get("mordred"))
    Battle.fight(knights.get("arthur"), knights.get("red_knight"))

    return Battle.results(knights)
