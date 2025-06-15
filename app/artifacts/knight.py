from app.artifacts.armour import Armour, ArmourPart
from app.artifacts.potion import Potion
from app.artifacts.weapon import Weapon
from app.battle_field.stats import Stats


class Knight:
    def __init__(self, knight_name: str, knight_power: int, knight_hp: int) -> None:
        self.name = knight_name
        self.power = knight_power
        self.hp = knight_hp
        self.armour = Armour()
        self.weapon = None
        self.potion = None

    def add_armour(self, armour_part: ArmourPart) -> None:
        self.armour.add_part(armour_part)

    def add_weapon(self, weapon: "Weapon"):
        self.weapon = weapon

    def add_potion(self, potion: "Potion"):
        self.potion = potion

    def get_stats(self) -> "Stats":
        knight_stats = Stats(self.hp, self.power, 0)

        knight_stats += self.armour.get_stats()

        if isinstance(self.weapon, Weapon):
            knight_stats += self.weapon.get_stats()

        if isinstance(self.potion, Potion):
            knight_stats += self.potion.get_stats()

        return knight_stats

