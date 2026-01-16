from typing import Optional


class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.base_power: int = config["power"]
        self.hp: int = config["hp"]
        self.armour: list[dict] = config.get("armour", [])
        self.weapon: dict = config["weapon"]
        self.potion: Optional[dict] = config.get("potion")

        self.power: int = self.base_power
        self.protection: int = 0
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.power += self.weapon["power"]
        self.protection += sum(part["protection"] for part in self.armour)

        if self.potion:
            for stat, effect in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + effect)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
