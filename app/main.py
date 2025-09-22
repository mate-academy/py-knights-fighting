from app.config.config import KNIGHTS
from app.characters.Knight import Knight
from app.actions.battle import take_battle


def prepare_knight(knight_data: dict) -> Knight:
    knight = Knight.create_character(knight_data)

    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()

    return knight


def battle(knights_config: dict):
    lancelot = prepare_knight(knights_config["lancelot"])
    arthur = prepare_knight(knights_config["arthur"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    take_battle(lancelot, mordred)
    take_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
