from typing import Optional, Dict


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list = [],
            weapon: Dict[str, any] = {},
            potion: Optional[Dict[str, any]] = None
    ) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: list = armour
        self.weapon: Dict[str, any] = weapon
        self.potion: Optional[Dict[str, any]] = potion

    def apply_effects(self) -> None:
        self.protection = sum(armor["protection"] for armor in self.armour)

        # Apply weapon
        self.power += self.weapon.get("power", 0)

        if self.potion is not None:
            effect = self.potion.get("effect", {})
            attributes_to_apply = ["power", "protection", "hp"]

            for attribute in attributes_to_apply:
                setattr(self, attribute, getattr(self, attribute, 0)
                        + effect.get(attribute, 0))
