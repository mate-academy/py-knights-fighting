from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: dict,
                 weapon: dict,
                 potion: dict,
                 protection: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    @classmethod
    def create_knight(cls, knights_data: dict) -> Knight:
        return Knight(
            name=knights_data["name"],
            power=knights_data["power"],
            hp=knights_data["hp"],
            armour=knights_data["armour"],
            weapon=knights_data["weapon"],
            potion=knights_data["potion"],
            protection=0
        )

    def apply_knight_stats(self: Knight) -> None:
        # apply armour
        for item in self.armour:
            self.protection += item["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def fight(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        # check if someone fell in battle
        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)
