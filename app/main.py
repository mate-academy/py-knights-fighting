from modules.knight import Knight
from modules.config import KNIGHTS
from modules.arsenal import Weapon, Armor, Potion


def battle(knights_config: dict) -> dict:
    list_of_knights = []

    for knight_data in knights_config.values():
        armor_list = [
            Armor(ar["part"], ar["protection"])
            for ar in knight_data["armour"]
        ]

        weapon = Weapon(
            knight_data["weapon"]["name"],
            knight_data["weapon"]["power"]
        )

        potion = (
            Potion(
                knight_data["potion"]["name"],
                knight_data["potion"]["effect"]
            )
            if knight_data["potion"] is not None else None
        )

        knight = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armor=armor_list,
            weapon=weapon,
            potion=potion
        )
        list_of_knights.append(knight)

    lancelot = list_of_knights[0]
    arthur = list_of_knights[1]
    mordred = list_of_knights[2]
    red_knight = list_of_knights[3]

    print("First Fight:")
    print()
    lancelot.fight_with(mordred)
    print()
    print("Other Fight:")
    print()
    arthur.fight_with(red_knight)
    print()

    res_dict = {"Lancelot": lancelot.hp, "Arthur": arthur.hp,
                "Mordred": mordred.hp, "Red Knight": red_knight.hp}

    return res_dict


if __name__ == "__main__":
    print(battle(KNIGHTS))
