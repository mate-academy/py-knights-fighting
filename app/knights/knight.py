"""Knight entity module."""

from typing import Any


class Knight:
    """Represents a knight participating in tournament combat."""

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict[str, Any]],
        weapon: dict[str, Any],
        potion: dict[str, Any] | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Knight":
        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data.get("armour", []),
            weapon=data["weapon"],
            potion=data.get("potion"),
        )

    def apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def fight(self, opponent: "Knight") -> None:
        damage_to_self = opponent.power - self.protection
        damage_to_opponent = self.power - opponent.protection

        self.take_damage(damage_to_self)
        opponent.take_damage(damage_to_opponent)
