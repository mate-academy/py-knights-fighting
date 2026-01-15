from typing import Dict


class Knight:
    def __init__(self, config: Dict) -> None:
        self.name: str = config["name"]
        self.power: int = config["power"]
        self.hp: int = config["hp"]
        self.armour: Dict = config["armour"]
        self.weapon: Dict = config["weapon"]
        self.potion: Dict = config["potion"]
        self.protection: int = self.apply_armour()
        self.power += self.weapon["power"]
        self.apply_potion()

    def apply_armour(self) -> int:
        protection: int = 0
        for part in self.armour:
            protection += part["protection"]
        return protection

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def battle(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp <= 0:
            self.hp = 0

        if opponent.hp <= 0:
            opponent.hp = 0
