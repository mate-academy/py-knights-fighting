from __future__ import annotations

from app.camelot.configs import POTION_EFFECTS


class Knight:
    def __init__(self, config: dict) -> None:
        self.protection = 0
        self.power = config["power"]
        self.name = config["name"]
        self.hp = config["hp"]
        self.apply_weapon(config)
        self.apply_armour(config)
        self.apply_potion(config)

    def apply_armour(self, config: dict) -> None:
        if armour := config.get("armour"):
            self.protection += sum([item["protection"] for item in armour])

    def apply_weapon(self, config: dict) -> None:
        if weapon := config.get("weapon"):
            self.power += weapon["power"]

    def apply_potion(self, config: dict) -> None:
        if potion := config.get("potion"):
            potion_effect = potion.get("effect")
            for effect in POTION_EFFECTS:
                if effect in potion_effect:
                    setattr(
                        self,
                        effect,
                        getattr(self, effect) + potion_effect.get(effect)
                    )

    def battle(self, other: Knight) -> dict:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0

        return {
            self.name: self.hp,
            other.name: other.hp,
        }
