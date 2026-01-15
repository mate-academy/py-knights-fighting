from app.knights.armour import Armour
from app.knights.khight import Knight
from app.knights.potion import Potion
from app.knights.weapon import Weapon


def get_prepared_knights(knights_data: dict[str, dict]) -> dict[str, Knight]:
    knights = {}

    for knight_name, knight_data in knights_data.items():
        armour = [
            Armour(
                part=armour_item.get("part"),
                protection=armour_item.get("protection"),
            )
            for armour_item in knight_data.get("armour")
        ]

        weapon = Weapon(
            name=knight_data.get("weapon").get("name"),
            power=knight_data.get("weapon").get("power"),
        )

        potion = None

        if knight_data.get("potion"):
            potion = Potion(
                name=knight_data.get("potion").get("name"),
                effect=knight_data.get("potion").get("effect"),
            )

        knight = Knight(
            name=knight_data.get("name"),
            power=knight_data.get("power"),
            hp=knight_data.get("hp"),
            armour=armour,
            weapon=weapon,
            potion=potion,
        )

        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

        knights[knight_name] = knight

    return knights
