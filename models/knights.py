from typing import TypedDict, Optional, List, Dict, Any


class ArmourDict(TypedDict):
    part: str
    protection: int


class WeaponDict(TypedDict):
    name: str
    power: int


class PotionEffectDict(TypedDict, total=False):
    power: int
    hp: int
    protection: int


class PotionDict(TypedDict):
    name: str
    effect: PotionEffectDict


class KnightDataDict(TypedDict):
    name: str
    power: int
    hp: int
    armour: List[ArmourDict]
    weapon: WeaponDict
    potion: Optional[PotionDict]


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]

        self.protection = 0

    def apply_armour(self) -> None:
        for item in self.armour:
            self.protection += item.get("protection", 0)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect", {})

            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()