from app.knight_stuff.weapon import Weapon
from app.knight_stuff.armour import Armour
from app.knight_stuff.potion import Potion


class Knight:

    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def __str__(self) -> str:
        if self.protection:
            return (
                f"Knight {self.name} has {self.power} power, "
                f"{self.hp} HP, {self.protection} protection."
            )
        else:
            return (
                f"Knight {self.name} has {self.power} power, {self.hp} HP"
            )

    def use_armour(self, armour: Armour) -> None:
        self.protection += armour.protection

    def use_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def use_potion(self, potion: Potion) -> None:
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]

    def count_hp(self, other: "Knight") -> int:
        hp = self.hp - (other.power - self.protection)
        if hp < 0:
            hp = 0
        return hp


def create_knight(name: str, knights_data: dict) -> Knight:

    knight = Knight(knights_data[name]["name"],
                    knights_data[name]["power"],
                    knights_data[name]["hp"])

    for armour_data in knights_data[name]["armour"]:
        armour = Armour(armour_data["part"], armour_data["protection"])
        knight.use_armour(armour)

    if knights_data[name]["potion"] is not None:
        potion = Potion(knights_data[name]["potion"]["name"],
                        knights_data[name]["potion"]["effect"])
        knight.use_potion(potion)

    if knights_data[name]["weapon"]:
        weapon = Weapon(knights_data[name]["weapon"]["name"],
                        knights_data[name]["weapon"]["power"])
        knight.use_weapon(weapon)

    return knight
