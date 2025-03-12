from app.config import KNIGHTS
from app.knight.knight import Knight
from app.battle import battle_logic
from typing import Dict


def _create_knight(knight_config: Dict) -> Knight:
    return Knight(
        name=knight_config["name"],
        power=knight_config["power"],
        hp=knight_config["hp"],
        armor_configs=knight_config["armour"],
        weapon_config=knight_config["weapon"],
        potion_config=knight_config["potion"],
    )


def battle(knights_config: Dict) -> Dict[str, int]:
    lancelot = _create_knight(knights_config["lancelot"])
    arthur = _create_knight(knights_config["arthur"])
    mordred = _create_knight(knights_config["mordred"])
    red_knight = _create_knight(knights_config["red_knight"])

    battle_logic(lancelot, mordred)
    battle_logic(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
