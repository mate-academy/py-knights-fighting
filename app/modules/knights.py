from __future__ import annotations


class Knight:
    knights = {}

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        Knight.knights.update({self.name : self})

    @staticmethod
    def make_knight(knights_dict: dict) -> None:

        for knight in knights_dict.values():

            name = knight["name"]
            power = knight["power"]
            hp = knight["hp"]
            protection = 0

            if knight["armour"]:
                for armour in knight["armour"]:
                    protection += armour["protection"]

            power += knight["weapon"]["power"]

            if knight["potion"]:
                effect_from_potion = knight["potion"]["effect"]

                if "protection" in effect_from_potion:
                    protection += effect_from_potion["protection"]

                if "power" in effect_from_potion:
                    power += effect_from_potion["power"]

                if "hp" in effect_from_potion:
                    hp += effect_from_potion["hp"]

            Knight(name, power, hp, protection)

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0
