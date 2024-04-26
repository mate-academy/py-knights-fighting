from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()
        self.use_potion()

    def calculate_protection(self) -> int:
        protection = 0
        for armour_part in self.armour:
            protection += armour_part["protection"]
        return protection

    def use_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def attack(self, opponent: Knight) -> None:
        damage = self.power + self.weapon["power"] - opponent.protection
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0
