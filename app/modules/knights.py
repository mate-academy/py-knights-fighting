from typing import Any


class Knight:
    knights_list = []

    def __init__(self, name: str, power: int, hp: int, protection: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        Knight.knights_list.append(self)

    @staticmethod
    def make_knight(knights_dict: dict) -> Any:

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
