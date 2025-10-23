from app.knights.equipment.weapon import Weapon
from app.knights.knights import Knights
from app.knights.participants.participants import lancelot_it, arthur_it, mordred_it, red_knight_it

KNIGHTS = Knights.knights_dict

def battle(knights_config):
    def battle_between(first_name: str, second_name: str) -> None:
        knights_config[first_name]["hp"] -= knights_config[second_name]["power"] - knights_config[first_name]["protection"]
        if knights_config[first_name]["hp"] < 0:
            knights_config[first_name]["hp"] = 0
        knights_config[second_name]["hp"] -= knights_config[first_name]["power"]- knights_config[second_name]["protection"]
        if knights_config[second_name]["hp"] < 0:
            knights_config[second_name]["hp"] = 0
        return None

    battle_between("lancelot", "mordred")
    battle_between("arthur", "red_knight")

    return {knights_config["lancelot"]["name"]: knights_config["lancelot"]["hp"],
        knights_config["arthur"]["name"]: knights_config["arthur"]["hp"],
        knights_config["mordred"]["name"]: knights_config["mordred"]["hp"],
        knights_config["red_knight"]["name"]: knights_config["red_knight"]["hp"]}



print(battle(KNIGHTS))
