from typing import Optional, Dict, List


class Knight:
    def __init__(self, name: str, base_hp: int, base_power: int,
                 armour: Optional[List[Dict[str, int]]],
                 weapon: Dict[str, int],
                 potion: Optional[Dict[str, Dict[str, int]]] = None) -> None:
        self.name = name
        self.hp = base_hp
        self.power = base_power + weapon.get("power", 0)
        self.protection = sum(item.get("protection", 0) for item in armour) if armour else 0
        self.weapon = weapon.get("name", "Unknown Weapon")
        self.potion = potion.get("name") if potion else None

        if potion and "effect" in potion:
            self.apply_potion(potion["effect"])

    def apply_potion(self, effect: Dict[str, int]) -> None:
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = max(opponent_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)

    def __repr__(self) -> str:
        return f"{self.name}(HP: {self.hp}, Power: {self.power}, Protection: {self.protection})"
