from typing import Optional, List


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: Optional[List[dict]] = None,
                 weapon: Optional[dict] = None,
                 potion: Optional[dict] = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

    @property
    def total_protection(self) -> int:
        protection = sum(part.get("protection", 0) for part in self.armour)
        if self.potion:
            protection += self.potion.get("effect", {}).get("protection", 0)
        return protection

    @property
    def total_power(self) -> int:
        weapon_power = self.weapon.get("power", 0) if self.weapon else 0
        power = self.power + weapon_power
        if self.potion:
            power += self.potion.get("effect", {}).get("power", 0)
        return power

    @property
    def total_hp(self) -> int:
        hp = self.hp
        if self.potion:
            hp += self.potion.get("effect", {}).get("hp", 0)
        return hp

    def to_stats(self) -> dict:
        return {
            "hp": self.total_hp,
            "power": self.total_power,
            "protection": self.total_protection,
        }
