from __future__ import annotations

from app.knights.ammunition import Armour, Potion, Weapon


class Knight:
    def __init__(
        self,
        name: str,
        tech_name: str,
        power: int,
        hp: int,
    ) -> None:
        self.name = name
        self.tech_name = tech_name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = None
        self.weapon = None
        self.potion = None

    @classmethod
    def knight_from_dict(cls, tech_name: str, knight_dict: dict) -> Knight:
        name = knight_dict["name"]
        power = knight_dict["power"]
        hp = knight_dict["hp"]
        return cls(name=name, tech_name=tech_name, power=power, hp=hp)

    @classmethod
    def knights_from_dict(cls, knights_list: list[dict]) -> Knight:
        return [
            cls.knight_from_dict(tech_name, knight)
            for tech_name, knight in knights_list.items()
        ]

    def apply_armour(self, armour: list[Armour] = None) -> None:
        if armour is not None:
            self.armour = armour
            for part in armour:
                self.protection += part.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def apply_potion(self, potion: Potion = None) -> None:
        if potion is not None:
            effects = potion.effects
            self.power += effects.get("power", 0)
            self.hp += effects.get("hp", 0)
            self.protection += effects.get("protection", 0)

    def __repr__(self) -> str:
        return (
            f"{{Knight: name={self.name}, "
            f"power={self.power}, hp={self.hp}, protection={self.protection}}}"
        )
