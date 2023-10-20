from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str = "",
            power: int = 0,
            hp: int = 0,
            armour: list[dict] | None = None,
            weapon: dict | None = None,
            potion: dict | None = None,
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.protection = 0
        self.potion = potion
        if potion:
            self.potion_effects = potion["effect"]
        self.calculate_protection()
        self.update_power()
        self.update_hp()

    # Convert armour points and potion effects into knight's protection
    def calculate_protection(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]
        if self.potion and "protection" in self.potion_effects:
            self.protection += self.potion_effects["protection"]

    # Convert weapon power and potion effects into knight's power
    def update_power(self) -> None:
        self.power += self.weapon["power"]
        if self.potion and "power" in self.potion_effects:
            self.power += self.potion_effects["power"]

    # Convert potion effects into knight's hp
    def update_hp(self) -> None:
        if self.potion and "hp" in self.potion_effects:
            self.hp += self.potion_effects["hp"]

    # Update knight's hp after the fight
    def fighting(self, other: Knight) -> None:
        if self == other:
            raise ValueError("Knights cannot fight themselves")
        self.hp = max(self.hp + self.protection - other.power, 0)
