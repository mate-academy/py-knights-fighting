from knights.knight import Knight
from items.items_init import InitItems


class Preparation:

    @staticmethod
    def apply_armour(knight: Knight) -> None:
        for element in knight.armour:
            knight.protection += element.protect

    @staticmethod
    def apply_weapon(knight: Knight) -> None:
        knight.power += knight.weapon.power

    @staticmethod
    def apply_potion(knight: Knight) -> None:
        if knight.potion:
            knight.protection += knight.potion.effect.get("protection", 0)
            knight.hp += knight.potion.effect.get("hp", 0)
            knight.power += knight.potion.effect.get("power", 0)

    @staticmethod
    def init_knight(name: str, knights_config: dict) -> Knight:
        knight = Knight(
            name.replace("_", " ").title(),
            knights_config.get(name.lower()).get("power"),
            knights_config.get(name.lower()).get("hp"),
            InitItems.init_armour(name, knights_config),
            InitItems.init_weapon(name, knights_config),
            InitItems.init_potion(name, knights_config)
        )
        return knight
