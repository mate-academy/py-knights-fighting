from typing import Optional, Dict, Any, List


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[List[Dict[str, Any]]] = None,
        weapon: Optional[Dict[str, Any]] = None,
        potion: Optional[Dict[str, Any]] = None
    ) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: List[Dict[str, Any]] = armour or []
        self.weapon: Dict[str, Any] = weapon or {}
        self.potion: Optional[Dict[str, Any]] = potion

    def apply_effects(self) -> None:
        self.protection = sum(
            armor.get("protection", 0) for armor in self.armour
        )
        self.power += self.weapon.get("power", 0)

        if self.potion is not None:
            effect = self.potion.get("effect", {})
            for attribute in ["power", "protection", "hp"]:
                setattr(
                    self,
                    attribute,
                    getattr(self, attribute, 0) + effect.get(attribute, 0)
                )
