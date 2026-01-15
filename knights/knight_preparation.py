from knights.knight import Knight


class Preparation:

    @staticmethod
    def apply_armour(knight: Knight) -> None:
        for element in knight.armour:
            knight.protection += element.protection

    @staticmethod
    def apply_weapon(knight: Knight) -> None:
        knight.power += knight.weapon.power

    @staticmethod
    def apply_potion(knight: Knight) -> None:
        if knight.potion:
            knight.protection += knight.potion.effect.get("protection", 0)
            knight.hp += knight.potion.effect.get("hp", 0)
            knight.power += knight.potion.effect.get("power", 0)
