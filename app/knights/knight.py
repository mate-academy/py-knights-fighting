from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def get_additional(self, knight_details: dict) -> None:
        # apply armour
        for part in knight_details["armour"]:
            self.protection += part["protection"]

        # apply weapon
        self.power += knight_details["weapon"]["power"]

        # apply potion if exist
        if knight_details["potion"]:
            if "power" in knight_details["potion"]["effect"]:
                self.power += knight_details["potion"]["effect"]["power"]

            if "protection" in knight_details["potion"]["effect"]:
                self.protection += (
                    knight_details["potion"]["effect"]["protection"]
                )

            if "hp" in knight_details["potion"]["effect"]:
                self.hp += knight_details["potion"]["effect"]["hp"]

    def __sub__(self, other: Knight) -> int:
        self.hp = self.hp - (other.power - self.protection)
        return max(self.hp, 0)
