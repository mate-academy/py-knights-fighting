from __future__ import annotations


class Knight:
    name = ""
    power = 0
    hp = 0
    protection = 0

    def __init__(self: Knight, name: str, knights_config: dict) -> None:
        knight_config = knights_config[name]
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        potions = knight_config["potion"]
        armour = knight_config["armour"]
        weapons = knight_config["weapon"]
        if potions:
            self.get_potions_stats(potions)
        if armour:
            self.get_protection(armour)
        if weapons:
            self.get_power(weapons)

    def __repr__(self: Knight) -> str:
        return (f"'name': '{self.name}', 'power': {self.power}, "
                f"'hp': {self.hp}, 'protection': {self.protection}")

    def get_potions_stats(self: Knight, potions: dict) -> None:
        effect = potions.get("effect", {})
        self.hp += effect.get("hp", 0)
        self.protection += effect.get("protection", 0)
        self.power += effect.get("power", 0)

    def get_protection(self: Knight, armour: list[dict]) -> None:
        self.protection += sum(item.get("protection", 0) for item in armour)

    def get_power(self: Knight, weapons: dict) -> None:
        self.power += weapons.get("power", 0)

    def __sub__(self: Knight, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
