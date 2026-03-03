from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: list[Armour] = []
        self.weapon: Weapon | None = None
        self.potion: Potion | None = None
        self.protection = 0

    def apply_armour(self, armour: list[dict]) -> None:
        self.armour = Armour.set_of_armour(armour)

    def apply_weapon(self, weapon: dict) -> None:
        self.weapon = Weapon(weapon["name"], weapon["power"])

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            new_potion = Potion(potion["name"])
            potion_effects = potion["effect"]
            if potion_effects.get("power"):
                new_potion.power_effect = potion_effects["power"]
            if potion_effects.get("protection"):
                new_potion.protection_effect = potion_effects["protection"]
            if potion_effects.get("hp"):
                new_potion.hp_effect = potion_effects["hp"]
            self.potion = new_potion

    def add_armour_protection(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part.protection

    def add_weapon_power(self) -> None:
        self.power += self.weapon.power

    def add_potion_effects(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.hp_effect
            self.power += self.potion.power_effect
            self.protection += self.potion.protection_effect
