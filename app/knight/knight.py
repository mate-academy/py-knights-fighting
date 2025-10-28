from __future__ import annotations
from app.equipment.equipment import Armour, Weapon, Potion


class Knight:
    """A class to represent a knight.

    :param name: The name of the knight.
    :type name: str
    :param power: The power of the knight.
    :type power: int
    :param hp: The health points of the knight.
    :type hp: int
    :param armour: The armour of the knight.
    :type armour: Armour | None
    :param weapon: The weapon of the knight.
    :type weapon: Weapon
    :param potion: The potion of the knight.
    :type potion: Potion | None
    """
    knights = dict()

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Armour | None,
        weapon: Weapon,
        potion: Potion | None,
    ) -> None:
        """Initializes a Knight object.

        :param name: The name of the knight.
        :type name: str
        :param power: The power of the knight.
        :type power: int
        :param hp: The health points of the knight.
        :type hp: int
        :param armour: The armour of the knight.
        :type armour: Armour | None
        :param weapon: The weapon of the knight.
        :type weapon: Weapon
        :param potion: The potion of the knight.
        :type potion: Potion | None
        """
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @classmethod
    def generate_knights(cls, knights_config: dict) -> None:
        """Generates knights from a configuration dictionary.

        :param knights_config:
            A dictionary containing the knight configurations.
        :type knights_config: dict
        """
        for knight, data in knights_config.items():
            armour = data.get("armour")
            potion = data.get("potion")
            cls.knights[knight] = cls(
                name=data.get("name"),
                power=data.get("power"),
                hp=data.get("hp"),
                armour=Armour(armour) if armour else None,
                weapon=Weapon(data.get("weapon")),
                potion=Potion(potion) if potion else None
            )

    @classmethod
    def apply_equipment(cls) -> None:
        """Applies the equipment to all knights."""
        for knight in Knight.knights.values():
            knight.weapon.apply_weapon(knight)
            if knight.armour:
                knight.armour.apply_armour(knight)
            if knight.potion:
                knight.potion.apply_potion(knight)
