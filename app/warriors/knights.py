from __future__ import annotations


class Knights:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
    ) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp

    def apply_armour(self, armours: list) -> Knights:
        for armour in armours:
            self.protection += armour["protection"]

    def apply_weapon(self, weapons: dict) -> Knights:
        self.power += weapons["power"]

    def apply_potion(self, potion: dict) -> Knights:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
