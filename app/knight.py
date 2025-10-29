from typing import Dict, List, Optional, Any


class Knight:
    """
    Represents a Knight character with specific
    attributes and abilities.

    The Knight class allows the creation of a knight
    character with particular attributes such as health
    points (hp), power, armor, weapon, and potion.
    The knight's overall characteristics (power, protection,
    and health) are calculated based on the base attributes,
    equipped items, and potion effects. The class also supports
    functionalities like taking damage and determining
    if the knight is still alive.

    """
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, Any]] = None,
            weapon: Dict[str, Any] = None,
            potion: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initializes a character with attributes
        defining its combat properties.

        The class constructor sets up the basic
        attributes such as name, base power,
        and base health points (HP). Optional
        arguments include a list of armour
        components, a weapon specification, and a potion.
        Based on these inputs, the class calculates effective
        health points, combat power, and protection level.

        :param name: The name of the character.
        :type name: str
        :param power: The base power level of the character.
        :type power: int
        :param hp: The base health points (HP) of the character.
        :type hp: int
        :param armour: A list of dictionaries, where each dictionary
            defines an armour item's properties such as type, defense
            value, and other attributes. If None, defaults to an empty list.
        :type armour: List[Dict[str, Any]]
        :param weapon: A dictionary defining the weapon's properties
            (e.g., type, damage). If None, defaults to an empty dictionary.
        :type weapon: Dict[str, Any]
        :param potion: An optional dictionary defining the potion's
            properties such as  type and effects. If None, it is omitted.
        :type potion: Optional[Dict[str, Any]]
        """
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon or {}
        self.potion = potion

        self.hp = self._calculate_hp()
        self.power = self._calculate_power()
        self.protection = self._calculate_protection()

    def _calculate_hp(self) -> int:
        """
        Calculates the total hit points (HP) for the
        character based on the base HP and any
        modifiers provided by an equipped potion.

        This method assesses the character's base HP
        and incrementally adds extra HP based on the
        potion's effect attribute if it is equipped
        and contains the appropriate key.

        :return: Calculated total HP integer of the
            character including potion effects.
        :rtype: int
        """
        hp = self.base_hp
        if self.potion and "effect" in self.potion:
            hp += self.potion["effect"].get("hp", 0)
        return hp

    def _calculate_power(self) -> int:
        """
        Calculates the total power by summing up the
        base power, the weapon's power if present,
        and any additional effects from a potion
        if applicable. Combines these attributes
        to determine the final value.

        :return: The total calculated power as an integer.
        :rtype: int
        """
        power = self.base_power

        if self.weapon:
            power += self.weapon.get("power", 0)

        if self.potion and "effect" in self.potion:
            power += self.potion["effect"].get("power", 0)

        return power

    def _calculate_protection(self) -> int:
        """
        Calculates the total protection for a character
        based on their equipped armour
        and the effects of a potion, if any.

        The protection is determined by summing
        the protection values present in each
        piece of armour and adding any protection
        effect provided by an active potion.

        :return: The total protection value calculated
            from armour and potion effects.
        :rtype: int
        """
        protection = 0

        for armour_part in self.armour:
            protection += armour_part.get("protection", 0)

        if self.potion and "effect" in self.potion:
            protection += self.potion["effect"].get("protection", 0)

        return protection

    def take_damage(self, damage: int) -> None:
        """
        Reduces the current health points (hp) of the
        object by the specified damage  value.
        Ensures that the hp does not go below zero.

        :param damage: The amount of damage to subtract
            from the current health points (hp).
        :type damage: int
        :return: None
        """
        self.hp = max(0, self.hp - damage)

    def is_alive(self) -> bool:
        """
        Check whether the entity is alive based
        on its current hit points.

        This method determines if the object has
        more than zero hit points (hp) and returns
        a boolean value to indicate its status.

        :return: True if the current hit points (hp)
            are greater than zero, otherwise False.
        :rtype: bool
        """
        return self.hp > 0

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "Knight":
        """
        Creates an instance of the class from a configuration
        dictionary. This method parses the given dictionary and
        initializes the class instance using the values
        provided. Non-mandatory attributes will be set to default
        values if not specified in the configuration dictionary.

        :param config: The configuration dictionary containing t
            he data to create the instance.

        :return: An instance of "Knight" initialized using the provided
            configuration.
        :rtype: Knight
        """
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config.get("armour", []),
            weapon=config.get("weapon", {}),
            potion=config.get("potion")
        )
