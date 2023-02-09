from app.data.knights_data import KNIGHTS
from app.classes.knights import Knight
from app.classes.arena import Arena


def battle(knights_dict: dict) -> dict:
    knights_instances = {}
    for name in knights_dict:
        knights_instances[name] = Knight(**knights_dict.get(name))
        knights_instances[name].gear_converter()

    Arena.fight_in_arena("lancelot_VS_mordred", knights_instances)
    Arena.fight_in_arena("arthur_VS_red_knight", knights_instances)

    Arena.death_check()

    return Arena.fighting_result


if __name__ == "__main__":
    print(battle(KNIGHTS))
