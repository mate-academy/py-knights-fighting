from __future__ import annotations


class Knight:
    def __init__(
            self, name: str,
            hp: int,
            power: int,
            weapon: dict,
            armour: list,
            potion: dict | None = None
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_power = power
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.apply_equipment()

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        return cls(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            weapon=data["weapon"],
            armour=data["armour"],
            potion=data["potion"]
        )

    def apply_equipment(self) -> None:
        self.power += self.weapon.get("power", 0)

        self.protection += sum(
            item.get("protection", 0) for item in self.armour
        )

        if self.potion:
            effect = self.potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def fight(self, opponent: "Knight") -> None:
        self_damage = max(opponent.power - self.protection, 0)
        opponent_damage = max(self.power - opponent.protection, 0)

        self.hp = max(self.hp - self_damage, 0)
        opponent.hp = max(opponent.hp - opponent_damage, 0)

    def __repr__(self) -> str:
        return (f"{self.name}: HP={self.hp}, "
                f"Power={self.power}, Protection={self.protection}")
