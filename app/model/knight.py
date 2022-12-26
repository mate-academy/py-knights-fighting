from app.model.armour import Armour
from app.model.potion import Potion
from app.model.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list[Armour], weapon: Weapon, potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def parse_knight_from_config(self, knightsConfig: dict) -> dict:
        knight = Knight()


    def calculate_final_stats(self):
        self.power += self.weapon.power + self.potion.get_effect_on_power()
        self.hp += self.potion.get_effect_on_hp()
        self.protection = sum([armour_piece.protection for armour_piece in self.armour])

    def check_if_fell_in_battle(self):
        if self.hp <= 0:
            self.hp = 0