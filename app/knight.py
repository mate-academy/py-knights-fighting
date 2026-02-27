from typing import Dict, Any


class Knight:
    def __init__(self, knight_config: Dict[str, Any]) -> None:
        self.name: str = knight_config["name"]
        self.hp: int = knight_config["hp"]
        self.power: int = knight_config["power"]
        self.protection: int = 0

        self._apply_armour(knight_config.get("armour", []))
        self._apply_weapon(knight_config["weapon"])
        self._apply_potion(knight_config.get("potion"))

    def _apply_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.protection += armour["protection"]

    def _apply_weapon(self, weapon: Dict[str, Any]) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: Dict[str, Any] | None) -> None:
        if not potion:
            return

        for stat, value in potion["effect"].items():
            setattr(self, stat, getattr(self, stat) + value)

    def take_damage(self, damage: int) -> None:
        damage = max(damage, 0)
        self.hp = max(self.hp - damage, 0)
