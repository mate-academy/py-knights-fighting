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
        self.check_hp()
        if "potion" in knight:
            self.potion()

    def potion(self) -> dict:
        potion_data = self.knight.get("potion") or {}
        effects = potion_data.get("effect", {})
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)
        self.hp += effects.get("hp", 0)
        return {"power": self.power,
                "hp": self.hp,
                "protection": self.protection}

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

    def fight(self, opponent: Knight) -> None:
        damage_to_self = max(opponent.power - self.protection, 0)
        self.hp -= damage_to_self
        self.check_hp()

    def check_hp(self) -> None:
        if self.hp < 0:
            self.hp = 0
