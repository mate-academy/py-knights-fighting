from __future__ import annotations


class KnightsFighting:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict | None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_equipment(self) -> KnightsFighting:
        self.power += self.weapon.get("power", 0)
        if any("protection" in arm for arm in self.armour):
            self.protection += sum(arm["protection"] for arm in self.armour)
        if self.potion:
            self.power += int(self.potion.get("effect", {}).get("power", 0))
            self.protection += int(
                self.potion.get("effect", {}).get("protection", 0))
            self.hp += int(self.potion.get("effect", {}).get("hp", 0))
        return self

    def get_hit(self, damage: KnightsFighting) -> None:
        self.hp -= damage.power - self.protection
        if self.hp <= 0:
            self.hp = 0
