from typing import List, Optional, Dict


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: Optional[List[Dict[str, int]]] = None,
        weapon: Optional[Dict[str, int]] = None,
        potion: Optional[Dict[str, Dict[str, int]]] = None,
    ) -> None:
        """
        Initialize a knight with its base attributes and equipment.

        :param name: The name of the knight.
        :param base_power: The base attack power of the knight.
        :param base_hp: The base health points of the knight.
        :param armour: A list of armour pieces, each with protection value.
        :param weapon: The knight's weapon with its power.
        :param potion: The knight's potion with its effects.
        """
        self.name: str = name
        self.base_power: int = base_power
        self.base_hp: int = base_hp
        self.armour: List[Dict[str, int]] = armour or []
        self.weapon: Optional[Dict[str, int]] = weapon
        self.potion: Optional[Dict[str, Dict[str, int]]] = potion

        # Calculated stats
        self.power: int = base_power
        self.hp: int = base_hp
        self.protection: int = 0

    def prepare_for_battle(self) -> None:
        """
        Prepare the knight for battle by applying armour,
         weapon, and potion effects.
        """
        self.protection = sum(piece["protection"] for piece in self.armour)
        if self.weapon:
            self.power += self.weapon["power"]

        if self.potion:
            effects = self.potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        """
        Reduce the knight's HP based on the opponent's
         attack power and its own protection.

        :param opponent_power: The attack power of the opponent.
        """
        damage: int = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)
