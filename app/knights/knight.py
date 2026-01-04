from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def health_points(
            self,
            armours: [dict],
            weapon: dict,
            potion: dict
    ) -> None:

        if armours:
            for armour in armours:
                self.protection += armour["protection"]

        if weapon:
            self.power += weapon["power"]

        if potion:
            for name_effect, effect in potion["effect"].items():
                if name_effect == "power":
                    self.power += effect
                if name_effect == "protection":
                    self.protection += effect
                if name_effect == "hp":
                    self.hp += effect

    def knights_battle(self, knight: Knight) -> dict:
        self.hp -= (knight.power - self.protection)
        knight.hp -= (self.power - knight.protection)

        if self.hp <= 0:
            self.hp = 0

        if knight.hp <= 0:
            knight.hp = 0

        return {
            self.name: self.hp,
            knight.name: knight.hp,
        }
