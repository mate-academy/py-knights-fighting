from app.knights_package import dict_of_knights
from app.knights_package import knights_class
from app.battle import battle as battle_mod


def battle(dict_knights: dict) -> dict:

    knights_dict_class = {
        key: knights_class.Knight(knight["name"], knight["power"],
                                   knight["hp"], knight["armour"],
                                   knight["weapon"], knight["potion"])
        for key, knight in dict_knights.items()
    }

    pairs = [["lancelot", "mordred"], ["arthur", "red_knight"]]

    return battle_mod.battle_of_knights(knights_dict_class, pairs)


if __name__ == "__main__":
    print(battle(dict_of_knights.KNIGHTS))
