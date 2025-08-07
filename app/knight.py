from typing import Optional, Dict, List


class Knight:
    def __init__(self, data: Dict) -> None:
        self.name: str = data["name"]
        self.base_power: int = data["power"]
        self.base_hp: int = data["hp"]
        self.armour: List[Dict] = data.get("armour", [])
        self.weapon: Dict = data.get("weapon", {})
        self.potion: Optional[Dict] = data.get("potion", None)

        # Stats after applying armour, weapon, potion
        self.power: int = self.base_power
        self.hp: int = self.base_hp
        self.protection: int = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, attack_power: int) -> None:
        damage = attack_power - self.protection
        if damage < 0:
            damage = 0  # protection fully blocks damage, no healing
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def __repr__(self) -> str:
        return (
            f"{self.name}(HP={self.hp}, "
            f"Power={self.power}, Protection={self.protection})"
        )
