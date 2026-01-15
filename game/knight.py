from typing import Dict, Any


class Knight:
    def __init__(self,
                 config: Dict[str, Any]) -> None:
        self.base_power: int = config["power"]
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0
        self.power = self.base_power

    def prepare_for_battle(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        real_damage = max(0, damage - self.protection)
        self.hp = max(0, self.hp - real_damage)

    def attack(self, other_knights: "Knight") -> None:
        other_knights.take_damage(self.power)
