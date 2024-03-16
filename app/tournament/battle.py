from __future__ import annotations

from app.warriors.armour import Armour
from app.warriors.knight import Knight
from app.warriors.potion import Potion
from app.warriors.weapon import Weapon


class Battle:
    def __init__(self, knights_config: dict) -> None:
        self.knights = {}
        for knight_params in knights_config.values():
            knight = self.prepare_knight(knight_params)
            self.knights[knight.name] = knight

    @staticmethod
    def prepare_knight(knight_params: dict) -> Knight:
        knight = Knight(knight_params["name"],
                        knight_params["power"],
                        knight_params["hp"])
        for equip in knight_params["armour"]:
            armour = Armour(equip["part"], equip["protection"])
            knight.take_armour(armour)
        weapon = Weapon(knight_params["weapon"]["name"],
                        knight_params["weapon"]["power"])
        if knight_params["potion"] is not None:
            potion = Potion(knight_params["potion"]["name"],
                            knight_params["potion"]["effect"])
            knight.take_potion(potion)
        knight.take_weapon(weapon)
        return knight

    def make_round(self) -> dict:
        self.knights["Lancelot"].fight(self.knights["Mordred"])
        self.knights["Arthur"].fight(self.knights["Red Knight"])
        result = {}
        for name, knight in self.knights.items():
            result[name] = knight.hp
        return result
