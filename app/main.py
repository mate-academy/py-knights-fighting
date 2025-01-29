from app.knights.preparations import Knight
from app.knights.information import KNIGHTS
from app.event.opponents import sparring


def battle(knight_config: dict) -> list:
    ready = []
    for name in knight_config:
        knight = knight_config[name]
        man = Knight(knight["name"], knight["power"], knight["hp"])
        man.get_armour(knight["armour"])
        man.get_weapon(knight["weapon"])
        man.get_potion(knight["potion"])
        ready.append(man)
    results = sparring(ready)
    return results


print(battle(KNIGHTS))
