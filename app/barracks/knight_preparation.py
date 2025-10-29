from typing import Dict, Optional
from app.barracks.equip import apply_equipment, apply_potion


class Knight:
    """Represents a knight with stats, equipment, and potions."""

    def __init__(self, config: Dict[str, any]) -> None:
        """Initialize knight stats and apply equipment and potion effects."""
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.base_power: int = config["power"]
        self.armour: list = config["armour"]
        self.weapon: Dict[str, int] = config["weapon"]
        self.potion: Optional[dict] = config.get("potion")

        self.power = self.base_power
        self.protection = 0

        apply_equipment(self)
        apply_potion(self)
