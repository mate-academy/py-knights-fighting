from typing import Dict, Any, List, Optional

class Knight:
    """Представляє лицаря, обчислює ефективні характеристики та обробляє шкоду."""

    def __init__(self, raw_data: Dict[str, Any]):
        self.name: str = raw_data["name"]
        self.hp: int = raw_data["hp"]
        self.base_power: int = raw_data["power"]
        
        self.armour: List[Dict[str, Any]] = raw_data["armour"]
        self.weapon: Dict[str, Any] = raw_data["weapon"]
        self.potion: Optional[Dict[str, Any]] = raw_data["potion"]
        
        self.protection: int = 0
        self.effective_power: int = 0
        
        self._calculate_effective_stats()

    def _calculate_effective_stats(self) -> None:
        """Розраховує HP, Силу та Захист на основі екіпірування/зілля."""
        
        self.protection = sum(part["protection"] for part in self.armour)
        self.effective_power = self.base_power + self.weapon["power"]
        
        if self.potion is not None:
            effects = self.potion["effect"]
            
            self.hp += effects.get("hp", 0)
            self.effective_power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        """Розраховує та застосовує отриману шкоду."""
        
        damage = max(0, opponent_power - self.protection)
        self.hp -= damage
        
        if self.hp < 0:
            self.hp = 0
