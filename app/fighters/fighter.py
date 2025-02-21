from app.fighters.armour import Armour
from app.fighters.potion import Potion
from app.fighters.weapon import Weapon


class Fighter:
    def __init__(
        self, name: str, power: int, hp: int, weapon: Weapon = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = []
        self.potion = None

    def add_armour(self, armour: Armour) -> None:
        self.armour.append(armour)

    def add_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def add_potion(self, potion: Potion) -> None:
        self.potion = potion

    def update_fighter(self) -> dict:
        total_hp = self.hp
        total_power = self.power + self.weapon.power
        total_protection = sum(a.protection for a in self.armour)

        if self.potion:
            if "hp" in self.potion.effect:
                total_hp += self.potion.effect["hp"]
            if "power" in self.potion.effect:
                total_power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                total_protection += self.potion.effect["protection"]

        return {
            "hp": total_hp,
            "power": total_power,
            "protection": total_protection,
        }
