from typing import Dict, Optional


class Knight:
    def __init__(self, stats: Dict) -> None:
        self.name = stats["name"]
        self.hp = stats["hp"]
        self.power = stats["power"]
        self.armour = stats.get("armour", [])
        self.weapon = stats["weapon"]
        self.option = stats.get("option")
        self.protection = 0
        self.potion: Optional[Dict] = stats.get("potion")
        self._prepare_for_battle()

    def _prepare_for_battle(self) -> None:
        for piece in self.armour:
            self.protection += piece["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
