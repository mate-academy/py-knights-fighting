from typing import Optional


class Knight:

    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: list[dict],
                 weapon: Optional[dict],
                 potion: dict | None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_power(self) -> int:
        total_power = self.power
        total_power += (self.weapon or {}).get("power", 0)
        total_power += (self.potion or {}).get("effect", {}).get("power", 0)
        return total_power

    def get_protection(self) -> int:
        total_protection = 0
        for protect in (self.armour or []):
            total_protection += protect.get("protection", 0)
        total_protection += ((self.potion or {})
                             .get("effect", {})
                             .get("protection", 0))
        return total_protection

    def get_hp(self) -> int:
        total_health = self.hp
        total_health += (self.potion or {}).get("effect", {}).get("hp", 0)
        return total_health

    def get_stats(self) -> dict:
        return {"name": self.name,
                "hp": self.get_hp(),
                "power": self.get_power(),
                "protection": self.get_protection()}
