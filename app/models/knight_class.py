from __future__ import annotations


class Knight:
    def __init__(self, indicators: dict) -> None:
        self.name = indicators["name"]
        self.power = indicators["power"]
        self.hp = indicators["hp"]
        self.armour = indicators.get("armour", [])
        self.weapon = indicators.get("weapon", {})
        self.potion = indicators.get("potion", None)
        self.protection = 0

    def apply_armor(self) -> Knight:
        self.protection = sum(
            part.get("protection", 0) for part in self.armour
        )
        return self

    def apply_weapon(self) -> Knight:
        self.power += self.weapon.get("power", 0)
        return self

    def apply_potion(self) -> Knight:
        if not self.potion:
            return None
        for stat, value in self.potion.get("effect").items():
            if stat == "power":
                self.power += value
            elif stat == "protection":
                self.protection += value
            elif stat == "hp":
                self.hp += value
        return self

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def fight(self, other: Knight) -> None:
        dmg_to_self = max(0, other.power - self.protection)
        dmg_to_other = max(0, self.power - other.protection)
        self.take_damage(dmg_to_self)
        other.take_damage(dmg_to_other)
