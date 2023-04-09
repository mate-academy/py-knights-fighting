from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list[dict] | list) -> Knight:
        if not armour:
            return self
        if armour is not []:
            for i in armour:
                self.protection += i.get("protection")
        return self

    def apply_weapon(self, weapon: dict) -> Knight:
        self.power += weapon.get("power")
        return self

    def apply_potion(self, potion: dict | None) -> Knight:
        if potion is not None:
            effect = potion.get("effect")
            if effect is not None:
                if "power" in effect:
                    self.power += effect.get("power")
                if "protection" in effect:
                    self.protection += effect.get("protection")
                if "hp" in effect:
                    self.hp += effect.get("hp")
            return self
        else:
            return self
