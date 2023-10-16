from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def power_weapon(self) -> None:
        self.power += self.weapon["power"]

    def hp_armour(self) -> None:
        protection = sum(part["protection"] for part in self.armour)
        self.hp += protection

    def use_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.hp += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def fight(self, other_knight: Knight) -> None:
        hp_first_knight = self.hp - other_knight.power
        hp_second_knight = other_knight.hp - self.power
        if hp_first_knight < 0:
            hp_first_knight = 0
        self.hp = hp_first_knight
        if hp_second_knight < 0:
            hp_second_knight = 0
        other_knight.hp = hp_second_knight
