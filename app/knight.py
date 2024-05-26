from typing import List, Dict


class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: List[Dict[str, int]],
            weapon: Dict[str, int],
            potion: Dict[str, Dict[str, int]] = None
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(piece["protection"] for piece in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            potion = self.potion.get("effect", {})
            for effect, value in potion.items():
                if effect == "power":
                    self.power += value
                elif effect == "protection":
                    self.protection += value
                elif effect == "hp":
                    self.hp += value

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
