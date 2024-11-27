from typing import Dict, Any


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Dict[str, int]],
            weapon: dict, potion:
            dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion if potion else {}

    def get_protection(self) -> int:
        return sum(part["protection"] for part in self.armour)

    def get_effective_power(self) -> int:
        weapon_power = self.weapon["power"]
        potion_power = self.potion.get("effect", {}).get("power", 0)
        return self.power + weapon_power + potion_power

    def get_effective_hp(self) -> int:
        potion_hp = self.potion.get("effect", {}).get("hp", 0)
        return self.hp + potion_hp

    def get_effective_protection(self) -> int:
        potion_protection = self.potion.get("effect", {}).get("protection", 0)
        return self.get_protection() + potion_protection


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    knights = {name: Knight(**data) for name, data in knights_config.items()}

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]

    lancelot_hp = (lancelot.get_effective_hp()
                   - max(mordred.get_effective_power()
                         - lancelot.get_effective_protection(),
                         0)
                   )
    mordred_hp = (mordred.get_effective_hp()
                  - max(lancelot.get_effective_power()
                        - mordred.get_effective_protection(),
                        0))

    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    arthur_hp = (arthur.get_effective_hp()
                 - max(red_knight.get_effective_power()
                       - arthur.get_effective_protection(),
                       0))
    red_knight_hp = (red_knight.get_effective_hp()
                     - max(arthur.get_effective_power()
                           - red_knight.get_effective_protection(),
                           0))

    return {
        "Lancelot": max(lancelot_hp, 0),
        "Arthur": max(arthur_hp, 0),
        "Mordred": max(mordred_hp, 0),
        "Red Knight": max(red_knight_hp, 0),
    }
