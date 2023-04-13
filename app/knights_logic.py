from typing import List, Dict, Any


class Knight:
    instances = {}

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[Dict[str, Any]],
                 weapon: Dict[str, Any],
                 potion: Dict[str, Any],
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.calculate_stats()

    def __str__(self) -> str:
        return (
            f"{'*' * 79}\n"
            f"name = {self.name}\n"
            f"power = {self.power}\n"
            f"hp = {self.hp}\n"
            f"armour = {self.armour}\n"
            f"weapon = {self.weapon}\n"
            f"potion = {self.potion}\n"
        )

    def calculate_stats(self) -> None:

        if self.armour:
            for part in self.armour:
                self.hp += part["protection"]
        self.power += self.weapon["power"]
        if self.potion:
            for stats in self.potion["effect"]:
                if "hp" in stats:
                    self.hp += self.potion["effect"]["hp"]
                if "protection" in stats:
                    self.hp += self.potion["effect"]["protection"]
                if "power" in stats:
                    self.power += self.potion["effect"]["power"]


def create_knights(knight_data_dict: Dict[str, Dict[str, Any]]) -> Knight:
    for knight in knight_data_dict.values():
        knight_class_obj = Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=knight["armour"],
            weapon=knight["weapon"],
            potion=knight["potion"]
        )
        Knight.instances[knight["name"]] = knight_class_obj
    return knight_class_obj


def duels() -> None:
    Knight.instances["Lancelot"].hp -= Knight.instances["Mordred"].power
    Knight.instances["Mordred"].hp -= Knight.instances["Lancelot"].power
    Knight.instances["Artur"].hp -= Knight.instances["Red Knight"].power
    Knight.instances["Red Knight"].hp -= Knight.instances["Artur"].power
    for knight in Knight.instances.values():
        knight.hp = 0 if knight.hp < 0 else knight.hp


def tournament_result() -> Dict[str, int]:
    return {
        "Lancelot": Knight.instances["Lancelot"].hp,
        "Artur": Knight.instances["Artur"].hp,
        "Mordred": Knight.instances["Mordred"].hp,
        "Red Knight": Knight.instances["Red Knight"].hp,
    }
