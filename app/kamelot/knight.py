from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list[dict], weapon: dict, potion: dict | None = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @classmethod
    def init_from_dict(cls, data: dict) -> list[Knight]:
        """Create a list of Knight objects from a dictionary."""
        knights = []
        for key, knight_data in data.items():
            knights.append(
                cls(
                    name=knight_data["name"],
                    power=knight_data["power"],
                    hp=knight_data["hp"],
                    armour=knight_data["armour"],
                    weapon=knight_data["weapon"],
                    potion=knight_data.get("potion"),
                )
            )
        return knights

    def battle_preparations(self, knights: list[Knight]) -> list[Knight]:
        pass

