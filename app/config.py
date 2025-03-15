from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.name = knight["name"]
        self.power = knight.get("power", 0)
        self.hp = knight["hp"]
        self.protection = 0
        self.sum_protection()
        self.knights_power()
        if "potion" in knight:
            self.potion()

    def potion(self) -> tuple[int, int, int]:
        potion_data = self.knight.get("potion") or {}
        effects = potion_data.get("effect", {})
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)
        self.hp += effects.get("hp", 0)
        return self.power, self.hp, self.protection

    def sum_protection(self) -> int:
        self.protection = 0
        if "armour" in self.knight:
            for armor in self.knight["armour"]:
                self.protection += armor.get("protection")
        return self.protection

    def knights_power(self) -> int:
        weapon_power = self.knight.get("weapon", {}).get("power", 0)
        self.power += weapon_power
        return self.power
