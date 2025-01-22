from typing import List, Optional, Dict


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[Dict[str, int]],
                 weapon: Dict[str, int],
                 potion: Optional[Dict[str, Dict[str, int]]]) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0

    def apply_armour(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self) -> None:
        self.power = self.base_power + self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def battle_damage(self, opponent: "Knight") -> None:
        self.hp -= max(0, opponent.power - self.protection)
        opponent.hp -= max(0, self.power - opponent.protection)
        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)

    def get_stats(self) -> Dict[str, int]:
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection
        }
