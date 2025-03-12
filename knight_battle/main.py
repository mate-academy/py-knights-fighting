from knight_battle.config import KNIGHTS
from knight_battle.knight.knight import Knight
from knight_battle.battle import battle_logic
from typing import Dict

def battle(knights_config: Dict) -> Dict[str, int]:
    lancelot_config = knights_config["lancelot"]
    arthur_config = knights_config["arthur"]
    mordred_config = knights_config["mordred"]
    red_knight_config = knights_config["red_knight"]

    lancelot = Knight(
        name=lancelot_config["name"],
        power=lancelot_config["power"],
        hp=lancelot_config["hp"],
        armor_configs=lancelot_config["armour"],
        weapon_config=lancelot_config["weapon"],
        potion_config=lancelot_config["potion"],
    )

    arthur = Knight(
        name=arthur_config["name"],
        power=arthur_config["power"],
        hp=arthur_config["hp"],
        armor_configs=arthur_config["armour"],
        weapon_config=arthur_config["weapon"],
        potion_config=arthur_config["potion"],
    )

    mordred = Knight(
        name=mordred_config["name"],
        power=mordred_config["power"],
        hp=mordred_config["hp"],
        armor_configs=mordred_config["armour"],
        weapon_config=mordred_config["weapon"],
        potion_config=mordred_config["potion"],
    )

    red_knight = Knight(
        name=red_knight_config["name"],
        power=red_knight_config["power"],
        hp=red_knight_config["hp"],
        armor_configs=red_knight_config["armour"],
        weapon_config=red_knight_config["weapon"],
        potion_config=red_knight_config["potion"],
    )

    battle_result_1 = battle_logic(lancelot, mordred)
    battle_result_2 = battle_logic(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
