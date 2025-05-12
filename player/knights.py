from player.data import data_character
import specifications
from specifications.protections import calculate_protection
from specifications.power import calculate_power
from specifications.hp import calculate_hp


class Knights:
    knights = []
    def __init__(self, name: str, power: str, hp: str, protection: str) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        Knights.knights.append(self)

    @staticmethod
    def character(knights_data: dict) -> list:
        for knight_data in knights_data.values():
            Knights(
                name=knight_data["name"],
                power=calculate_power(knight_data["potion"], (knight_data["power"] + knight_data["weapon"]["power"])),
                hp=calculate_hp(knight_data["potion"], knight_data["hp"]),
                protection=calculate_protection(knight_data["armour"], knight_data["potion"])
            )
        return Knights.knights
