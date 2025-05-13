from models.equipment import Weapon, Armour, Potion


class Knight:
    def __init__(self, name: str, base_power: int, base_hp: int) -> None:
        self.name = name
        self.hp = base_hp
        self.power = base_power
        self.protection = 0
        # equipment
        self.armour = []
        self.weapon = None
        self.potion = None

    def set_armor(self, armour: list[Armour]) -> None:
        self.armour = armour
        self.protection += sum(piece.protection for piece in armour)

    def set_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        self.potion = potion
        self.hp += potion.effect.get("hp", 0)
        self.power += potion.effect.get("power", 0)
        self.protection += potion.effect.get("protection", 0)
