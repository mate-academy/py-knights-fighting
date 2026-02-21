from object.armour import Armour
from object.potion import Potion
from object.knight import Knight
from object.weapon import Weapon


class Action:
    @staticmethod
    def knight_fight(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection
        for knight in (first_knight, second_knight):
            if knight.hp <= 0:
                knight.hp = 0

    @staticmethod
    def apply_armour(knights_list: list[Knight]) -> None:
        for knight in knights_list:
            final_protection = 0
            for part in knight.armour:
                final_protection += part.protection
            knight.protection = final_protection

    @staticmethod
    def apply_potion(knights_list: list[Knight]) -> None:
        for knight in knights_list:
            if knight.potion:
                for stat in knight.potion.effect:
                    value_before = getattr(knight, stat)
                    setattr(knight,
                            stat,
                            value_before + knight.potion.effect.get(stat))

    @staticmethod
    def create_knight(knight_config: dict) -> list[Knight]:
        knights_list = []
        for knight in knight_config.values():
            potion = knight.get("potion")
            knights_list.append(
                Knight(
                    name=knight.get("name"),
                    hp=knight.get("hp"),
                    power=knight.get("power"),
                    armour=[
                        Armour(armour.get("part"), armour.get("protection"))
                        for armour in knight.get("armour")],
                    potion=Potion(potion.get("name"),
                                  potion.get("effect")) if potion else None,
                    weapon=Weapon(knight.get("weapon").get("name"),
                                  knight.get("weapon").get("power"))
                )
            )
        return knights_list

    @staticmethod
    def apply_weapon(knight_list: list[Knight]) -> None:
        for knight in knight_list:
            knight.power += knight.weapon.power
