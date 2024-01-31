from __future__ import annotations


class Knight:
    dictionary_of_knights = dict()

    def __init__(self, name: str, hp: int,
                 power: int, protection: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
        Knight.dictionary_of_knights[self.name] = self

    @staticmethod
    def create_knight(input_dict_of_knights: dict) -> None:
        hp = 0
        power = 0
        protection = 0
        for knight in input_dict_of_knights.values():
            name = knight["name"]
            if knight["potion"] is not None:
                if "hp" in knight["potion"]["effect"].keys():
                    hp = knight["hp"] + knight["potion"]["effect"]["hp"]
                if "power" in knight["potion"]["effect"].keys():
                    power = (knight["power"] + knight["weapon"]["power"]
                             + knight["potion"]["effect"]["power"])
                if "protection" in knight["potion"]["effect"].keys():
                    protection = knight["potion"]["effect"]["protection"]
                if len(knight["armour"]) != 0:
                    for dic in knight["armour"]:
                        protection += dic["protection"]
            else:
                hp = knight["hp"]
                power = knight["power"] + knight["weapon"]["power"]
                if len(knight["armour"]) != 0:
                    for dic in knight["armour"]:
                        protection += dic["protection"]
            Knight(name, hp, power, protection)
            protection = 0
