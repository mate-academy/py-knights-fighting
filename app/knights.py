from typing import Optional, Dict


class Knight:
    def __init__(self, knight_info: Dict[str, any]) -> None:
        self.name: str = knight_info["name"]
        self.power: int = knight_info["power"]
        self.hp: int = knight_info["hp"]
        self.armour: list = knight_info.get("armour", [])
        self.weapon: Dict[str, any] = knight_info.get("weapon", {})
        self.potion: Optional[Dict[str, any]] = knight_info.get("potion", None)

    def apply_effects(self) -> None:
        # apply armour
        self.protection = sum(armor["protection"] for armor in self.armour)

        # apply weapon
        self.power += self.weapon.get("power", 0)

        # apply potion if exists
        if self.potion is not None:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)
