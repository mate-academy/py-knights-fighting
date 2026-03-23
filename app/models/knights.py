from app.models.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_equipment(
            self,
            weapon: Weapon,
            armours: list[Armour],
            potion: Potion
    ) -> None:

        self.power += weapon.power

        for armour_item in armours:
            self.protection += armour_item.protection

        if potion:
            self.hp += potion.effect.get("hp", 0)
            self.power += potion.effect.get("power", 0)
            self.protection += potion.effect.get("protection", 0)
