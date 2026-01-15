from app.config.config import KNIGHTS
from app.characters.Knight import Knight
from app.actions.battle import take_battle


def prepare_knight(knight_data: dict) -> Knight:
    knight = Knight.create_character(knight_data)

    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()

    return knight


def battle(knights_config: dict) -> dict:
    knights = {name: prepare_knight(cfg) for name, cfg in
               knights_config.items()}

    lancelot = knights.get("lancelot")
    arthur = knights.get("arthur")
    mordred = knights.get("mordred")
    red_knight = knights.get("red_knight")

    take_battle(lancelot, mordred)
    take_battle(arthur, red_knight)

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
