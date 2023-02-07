from app.people.warriors import Knight
from app.ammunition.armours import Armour
from app.ammunition.potions import Potion
from app.ammunition.weapons import Weapon


def preparations(config: dict) -> dict:
    prepare_knights_list = {}
    for knight_name, knight_data in config.items():
        armour_list = []
        if knight_data.get("armour"):
            for armour in knight_data.get("armour"):
                armour_list.append(Armour(armour.get("part"),
                                          armour.get("protection")))

        weapon = Weapon(knight_data.get("weapon").get("name"),
                        knight_data.get("weapon").get("power"))

        knight = Knight(
            name=knight_data.get("name"),
            power=knight_data.get("power"),
            hp=knight_data.get("hp"),
        )

        knight.add_armour(armour_list)
        knight.add_weapon(weapon)

        if knight_data.get("potion"):
            potion = Potion(knight_data.get("potion").get("name"),
                            knight_data.get("potion").get("effect"))
            knight.add_potion(potion)

        prepare_knights_list[knight.name] = knight

    return prepare_knights_list
