from __future__ import annotations


class Knight:
    """
    Class representing a knight in the battle.
    Attributes:
        name (str): The name of the knight.
        power (int): The power of the knight.
        hp (int): The health points of the knight.
        armour (list): A list of armour pieces the knight has.
        weapon (dict): The weapon the knight has.
        potion (dict | None): The potion the knight has, if any.
    Methods:
        apply_armour(): Calculates the total protection
            from the knight's armour.
        apply_weapon(): Adds the weapon's power
            to the knight's power.
        apply_potion(): Applies the effects of the
            potion to the knight's attributes.
    """

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict | None = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return
        for effect, value in self.potion["effect"].items():
            setattr(self, effect, getattr(self, effect) + value)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def receive_attack(self, attacker: Knight) -> None:
        self.hp -= attacker.power - self.protection
        if self.hp <= 0:
            self.hp = 0
