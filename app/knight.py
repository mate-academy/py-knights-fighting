from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    weapon_power: int
    armour_protection: int
    potion_effect: Dict[str, int] = field(default_factory=dict)
    protection: int = 0

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "Knight":
        armour_protection = sum(
            item["protection"]
            for item in config["armour"]
        )

        potion = config.get("potion")
        potion_effect = {}

        if potion is not None:
            potion_effect = potion.get("effect", {})

        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            weapon_power=config["weapon"]["power"],
            armour_protection=armour_protection,
            potion_effect=potion_effect,
        )

    def prepare_for_battle(self) -> None:
        self.protection = self.armour_protection
        self.power += self.weapon_power

        self.power += self.potion_effect.get("power", 0)
        self.protection += self.potion_effect.get("protection", 0)
        self.hp += self.potion_effect.get("hp", 0)

    def take_damage_from(self, enemy: "Knight") -> None:
        damage = enemy.power - self.protection
        self.hp = max(self.hp - damage, 0)
