import app.items.armour as armour
import app.items.weapons as weapons
import app.items.potions as potions

class Knight:
    def __init__(self, profile: dict) -> None:
        self.name = profile["name"]
        self.power = profile["power"]
        self.hp = profile["hp"]
        self.protection = 0

    def apply_equipment(
            self,
            power_equipment: weapons.Weapon,
            protection_equipment: armour.Armour
    ) -> None:
        self.protection += protection_equipment.total_equipment_protection()
        self.power += power_equipment.power

    def apply_potion(self, potion: potions.Potion) -> None:
        for key in self.__dict__.keys():
            if hasattr(potion, key) and key != "name":
                setattr(self, key, getattr(self, key) + getattr(potion, key))
