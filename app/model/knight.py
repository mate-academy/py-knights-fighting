from __future__ import annotations

from app.model.armour import Armour
from app.model.potion import Potion
from app.model.weapon import Weapon


class Knight:
    name = ""
    power = 0
    hp = 0
    armour = []
    weapon = None
    potion = None

    def __init__(self) -> None:
        self.protection = None

    @staticmethod
    def parse_knight_stats(name: str, knights_config: dict) -> Knight:
        knight = Knight()
        knight.name = knights_config.get(name).get("name")
        knight.power = knights_config.get(name).get("power")
        knight.hp = knights_config.get(name).get("hp")
        knight.armour = Armour.parse_armour(knights_config.get(name)
                                            .get("armour"))
        knight.weapon = Weapon.parse_weapon(knights_config.get(name)
                                            .get("weapon"))
        knight.potion = Potion.parse_potion(knights_config.get(name)
                                            .get("potion"))
        return knight

    def calculate_final_stats(self) -> None:
        self.power += self.weapon.power + self.potion.get_effect_on_power()
        self.hp += self.potion.get_effect_on_hp()
        self.protection = sum(
            [armour_piece.protection for armour_piece in self.armour]) \
            + self.potion.get_effect_on_protection()

    def check_if_fell_in_battle(self) -> None:
        if self.hp <= 0:
            self.hp = 0
