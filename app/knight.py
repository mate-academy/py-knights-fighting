from __future__ import annotations


class Knights:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def preparation(self) -> None:
        for armour in self.armour:
            self.protection += armour.get("protection")

        if self.power:
            self.power += self.weapon.get("power")

        if self.potion:
            for key in self.potion.get("effect"):
                effect_value = getattr(self,
                                       key) + self.potion.get("effect")[key]
                setattr(self, key, effect_value)

    def fight(self, other: Knights) -> None:
        self.hp = max(0, self.hp - (other.power - self.protection))
        other.hp = max(0, other.hp - (self.power - other.protection))
