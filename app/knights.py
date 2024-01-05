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
        # Apply armour
        self.protection = sum(armor["protection"] for armor in self.armour)

        # Apply weapon
        self.power += self.weapon.get("power", 0)

        # Apply potion if exists
        if self.potion is not None:
            effect = self.potion.get("effect", {})
            attributes_to_apply = ["power", "protection", "hp"]

            for attribute in attributes_to_apply:
                setattr(self, attribute, getattr(self, attribute, 0)
                        + effect.get(attribute, 0))
