import app.classes
from app.classes.knights import Knight
from app.classes.arena import Arena




def battle(knights_dict: dict) -> dict:
    knights_instances = {}
    for name in knights_dict:
        knights_instances[name] = Knight(**knights_dict.get(name))
        knights_instances[name].gear_converter()

    Arena.fight_in_arena(
        knights_instances["lancelot"],
        knights_instances["mordred"]
    )
    Arena.fight_in_arena(
        knights_instances["arthur"],
        knights_instances["red_knight"]
    )

    return Arena.fighting_result


if __name__ == '__main__':
    print(battle(app.classes.KNIGHTS))
