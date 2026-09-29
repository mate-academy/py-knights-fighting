from typing import Optional


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        self._apply_armour(config.get("armour", []))
        self._apply_weapon(config.get("weapon"))
        self._apply_potion(config.get("potion"))

    def _apply_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.protection += armour["protection"]

    def _apply_weapon(self, weapon: Optional[dict]) -> None:
        if weapon:
            self.power += weapon["power"]

    def _apply_potion(self, potion: Optional[dict]) -> None:
        if potion and "effect" in potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
