from typing import Dict, List, Optional


class Knight:
    """Classe representando um cavaleiro."""

    def __init__(self, name: str, power: int, hp: int,
                 armour: Optional[List[Dict[str, int]]] = None,
                 weapon: Optional[Dict[str, int]] = None,
                 potion: Optional[Dict[str, Dict[str, int]]] = None) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: List[Dict[str, int]] = armour if armour else []
        self.weapon: Optional[Dict[str, int]] = weapon
        self.potion: Optional[Dict[str, Dict[str, int]]] = potion
        self.protection: int = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        """Aplica a proteção da armadura ao cavaleiro."""
        self.protection = sum(piece.get("protection", 0)
                              for piece in self.armour)

    def apply_weapon(self) -> None:
        """Adiciona o poder da arma ao cavaleiro."""
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        """Aplica efeitos da poção no cavaleiro, se houver."""
        if self.potion:
            effects: Dict[str, int] = self.potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
