from typing import Any


class Knights:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armor: list[dict | None],
                 weapon: dict,
                 potion: Any,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def add_equipment(self) -> None:
        # add ammunition
        for ammunition in self.armor:
            self.protection += ammunition["protection"]

        # add weapon
        self.power += self.weapon["power"]

        # add potion
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
