from app.models.Armour import Armour
from app.models.Potion import Potion
from app.models.Weapon import Weapon
import copy

class Knight:
    def __init__(self, name, base_power, base_hp, weapon, armour=None, potions=None, apply_potions=True):
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.base_protection = 0
        self.armour = armour if armour else []
        self.weapon = weapon
        self.potions = potions if potions else []

        # поточні стати
        self.power = base_power
        self.hp = base_hp

        # прапорець, що ефекти зілля застосовані
        self.buffs_applied = False

    @classmethod
    def from_dict(cls, data, apply_potions=True):
        data = copy.deepcopy(data)
        weapon = Weapon.from_dict(data["weapon"])
        armour_list = [Armour.from_dict(a) for a in data.get("armour", [])]

        potions_data = data.get("potions") or data.get("potion") or []

        # Якщо це один словник — обгортаємо в список
        if isinstance(potions_data, dict):
            potions_data = [potions_data]

        # Якщо None — ігноруємо
        if potions_data is None:
            potions_data = []

        potions = [Potion.from_dict(p) for p in potions_data if p]

        return cls(
            name=data.get("name", "Unknown Knight"),
            base_power=data.get("power", 0),
            base_hp=data.get("hp", 0),
            weapon=weapon,
            armour=armour_list,
            potions=potions,
            apply_potions=apply_potions
        )

    def apply_potion_effects(self):
        if self.buffs_applied:
            return  # ефекти вже застосовані

        self.power = self.base_power + (self.weapon.power if self.weapon else 0)
        self.base_protection = sum(part.protection for part in self.armour)

        for potion in self.potions:
            if potion and potion.effect:
                eff = potion.effect
                self.power += eff.power
                self.base_protection += eff.protection
                self.hp += eff.hp

        if self.hp < 0:
            self.hp = 0

        self.buffs_applied = True

    def total_attack(self):
        return self.power

    def total_defence(self):
        return self.base_protection

    def __str__(self):
        return (f"Knight {self.name}: HP={self.hp}, "
                f"Attack={self.total_attack()}, "
                f"Defence={self.total_defence()}")



