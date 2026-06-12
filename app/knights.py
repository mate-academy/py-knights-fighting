from __future__ import annotations
try:
    from equip.weapons import Weapon
    from equip.potions import Potion
except ImportError:
    from app.equip.weapons import Weapon
    from app.equip.potions import Potion


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.protection = 0
        for armour in knight_data["armour"]:
            self.protection += armour["protection"]
        self.weapon = Weapon(knight_data["weapon"])
        self.potion = (
            Potion(knight_data["potion"])
            if knight_data["potion"] else None
        )

        self.power += self.weapon.power

        if self.potion:
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection

    def fight(self, other: Knight) -> None:
        other.hp -= (self.power - other.protection)
        self.hp -= (other.power - self.protection)
        if other.hp <= 0:
            other.hp = 0
        if self.hp <= 0:
            self.hp = 0
