from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.apply_power()
        self.apply_armour()
        self.apply_potion()

    # def __init__(self, data: dict) -> Knight:
    #     self.name=data["name"],
    #     self.power=data["power"],
    #     self.hp=data["hp"],
    #     self.armour=data["armour"],
    #     self.weapon=data["weapon"],
    #     self.potion=data.get("potion")

    def apply_armour(self) -> None:
        self.protection = 0
        for ar in self.armour:
            self.protection += ar["protection"]

    def apply_power(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
