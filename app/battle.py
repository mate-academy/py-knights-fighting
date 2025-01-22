from typing import Dict
from app.knights import Knight


class Battle:
    def __init__(self, knights_config: Dict[str, Dict]) -> None:
        self.knights: Dict[str, Knight] = {
            name: Knight(
                name=knight["name"],
                power=knight["power"],
                hp=knight["hp"],
                armour=knight["armour"],
                weapon=knight["weapon"],
                potion=knight["potion"]
            )
            for name, knight in knights_config.items()
        }

    def prepare_knights(self) -> None:
        for knight in self.knights.values():
            knight.apply_armour()
            knight.apply_weapon()
            knight.apply_potion()

    def fight(self) -> None:
        self.knights["lancelot"].battle_damage(self.knights["mordred"])
        self.knights["arthur"].battle_damage(self.knights["red_knight"])

    def get_results(self) -> Dict[str, int]:
        return {
            knight.get_stats()["name"]: knight.get_stats()["hp"]
            for knight in self.knights.values()
        }
