from typing import Any


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int,
            armour: list[dict],
            weapon: dict[str, str | int],
            potion: dict[str, Any]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def sum_buffs(data: dict) -> None:
        data["protection"] = 0
        if potion := data.get("potion"):
            for key, value in potion.get("effect").items():
                data[key] += value
        data["power"] += data.get("weapon").get("power")
        for part in data.get("armour"):
            data["protection"] += part.get("protection")

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        cls.sum_buffs(data)
        return cls(**data)
