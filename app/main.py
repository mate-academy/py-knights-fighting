from app.combat import Arena
from app.preparation import Knight
from app.knights import KNIGHTS


def battle(knights: dict) -> dict:
    knights_instances = {}
    for knight_name, knight_data in knights.items():
        knight_instance = Knight(knight_data["name"],
                                 knight_data["power"],
                                 knight_data["hp"])
        knight_instance.use_weapon(knight_data["weapon"]["power"])
        knight_instance.use_armour(knight_data["armour"])
        knight_instance.use_potion(knight_data["potion"])
        knights_instances[knight_name] = knight_instance

    fight_1 = Arena.fight(knights_instances["lancelot"],
                          knights_instances["mordred"])
    fight_2 = Arena.fight(knights_instances["arthur"],
                          knights_instances["red_knight"])

    return {**fight_1, **fight_2}


print(battle(KNIGHTS))
