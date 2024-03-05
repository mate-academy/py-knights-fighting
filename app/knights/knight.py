from __future__ import annotations

from app.armor.ammunition import Armour, Weapon, Potion


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
    def one_knight(cls, tech_name: str, knight_dict: dict) -> Knight:
        name = knight_dict["name"]
        power = knight_dict["power"]
        hp = knight_dict["hp"]

        return cls(name=name, tech_name=tech_name, power=power, hp=hp)

    @classmethod
    def all_knights(cls, knights_list: list[dict]) -> list[Knight]:
        return [
            cls.one_knight(tech_name, knight)
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
            effects = potion.effect
            if "power" in effects:
                self.power += effects["power"]
            if "hp" in effects:
                self.hp += effects["hp"]
            if "protection" in effects:
                self.protection += effects["protection"]

    def __repr__(self) -> str:
        return (
            f"{{Knight: name={self.name}, "
            f"power={self.power}, hp={self.hp}, protection={self.protection}}}"
        )
