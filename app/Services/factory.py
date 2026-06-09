from app.Objects.weapon import Weapon
from app.Objects.potion import Potion
from app.Objects.armour import Armour
from app.Objects.knight import Knight


class KnightFactory:

    @staticmethod
    def create_weapon(weapon_data: dict) -> Weapon:
        return Weapon(
            name=weapon_data["name"],
            power=weapon_data["power"]
        )

    @staticmethod
    def create_armour(armour_data: list) -> list:
        armour_list = []

        for a in armour_data:
            armour_list.append(
                Armour(
                    part=a["part"],
                    protection=a["protection"]
                )
            )

        return armour_list

    @staticmethod
    def create_potion(potion_data: dict) -> Potion:
        if potion_data is None:
            return None
        return Potion(
            name=potion_data["name"],
            effect=potion_data["effect"]
        )

    @staticmethod
    def create_knight(knight_data: dict) -> Knight:
        weapon = KnightFactory.create_weapon(knight_data["weapon"])
        armour = KnightFactory.create_armour(knight_data["armour"])
        potion_data = knight_data.get("potion")
        potion = KnightFactory.create_potion(potion_data) if potion_data else None

        knight = Knight(
            name=knight_data["name"],
            hp=knight_data["hp"],
            power=knight_data["power"],
            weapon=weapon,
            armour=armour,
            potion=potion,
        )

        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion(potion)

        return knight

    @staticmethod
    def create_knights(knights_data: dict) -> dict:
        knights = {}

        for key, knight_data in knights_data.items():
            knight = KnightFactory.create_knight(knight_data)
            knights[key] = knight

        return knights
