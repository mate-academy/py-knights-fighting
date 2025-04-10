from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = None
        self.armour = []
        self.potion = None
        self.protection = 0

    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def equip_armour(self, armour: Armour) -> None:
        self.armour.append(armour)
        self.protection += armour.protection

    def equip_potion(self, potion: Potion) -> None:
        self.potion = potion
        if hasattr(potion, "power"):
            self.power += potion.power
        if hasattr(potion, "hp"):
            self.hp += potion.hp
        if hasattr(potion, "protection"):
            self.protection += potion.protection

    def fight(self, other: "Knight") -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0

    @classmethod
    def new_knight(cls, knight_config: dict) -> "Knight":

        knight = cls(knight_config["name"],
                     knight_config["power"],
                     knight_config["hp"])

        knight.equip_weapon(Weapon(knight_config["weapon"]["name"],
                            knight_config["weapon"]["power"]))

        for armour in knight_config["armour"]:

            knight.equip_armour(Armour(armour["part"],
                                armour["protection"]))

        if knight_config["potion"]:

            knight.equip_potion(Potion(knight_config["potion"]["name"],
                                knight_config["potion"]["effect"]))

        return knight
