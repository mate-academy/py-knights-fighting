from typing import Dict, Any, Optional
from app.extraction.extraction_first_dict import extract_first_dict


class Knight:
    def __init__(self, knight_data: Dict[str, Dict[str, Any]]) -> None:
        self.knight_data: Dict[str, Dict[str, Any]] = knight_data
        self.name: str = ""
        self.total_hp: int = 0
        self.total_power: int = 0
        self.total_protection: int = 0
        self._initialize_stats()

    def _initialize_stats(self) -> None:
        first_dict: Dict[str, Any] = extract_first_dict(self.knight_data)
        key, data = next(iter(first_dict.items()))
        self.name = data.get("name", key)

        base_hp: int = data.get("hp", 0)
        base_power: int = data.get("power", 0)
        weapon_power: int = data.get("weapon", {}).get("power", 0)
        armour_list: list = data.get("armour", [])
        total_protection: int = sum(a.get("protection", 0)
                                    for a in armour_list)

        potion: Optional[Dict[str, Any]] = data.get("potion")
        potion_hp: int = potion.get("effect", {}).get("hp", 0) if potion else 0
        potion_power: int = potion.get("effect", {}).get("power", 0) \
            if potion else 0
        potion_protection: int = (
            potion.get("effect", {}).get("protection", 0)) \
            if potion else 0

        self.total_hp = base_hp + potion_hp
        self.total_power = base_power + weapon_power + potion_power
        self.total_protection = total_protection + potion_protection

    def take_damage(self, damage: int) -> None:
        self.total_hp = max(0, self.total_hp - damage)
