from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.knight.knight import Knight


class Armour:
    """A class to represent armour for a knight.

    :param armour:
        A list of dictionaries, each representing a part of the armour.
    :type armour: list[dict[str, str | int]]
    """
    def __init__(self, armour: list[dict[str, str | int]]) -> None:
        """Initializes an Armour object.

        :param armour:
            A list of dictionaries, each representing a part of the armour.
        :type armour: list[dict[str, str | int]]
        """
        self.parts = [part.get("part") for part in armour]
        self.protection = sum([part.get("protection", 0) for part in armour])

    def apply_armour(self, knight: "Knight") -> None:
        """Applies the armour's protection to the knight.

        :param knight: The knight to apply the armour to.
        :type knight: Knight
        """
        knight.protection += self.protection


class Weapon:
    """A class to represent a weapon for a knight.

    :param weapon: A dictionary representing the weapon.
    :type weapon: dict[str, str | int]
    """
    def __init__(self, weapon: dict[str, str | int]) -> None:
        """Initializes a Weapon object.

        :param weapon: A dictionary representing the weapon.
        :type weapon: dict[str, str | int]
        """
        self.name = weapon.get("name")
        self.power = weapon.get("power")

    def apply_weapon(self, knight: "Knight") -> None:
        """Applies the weapon's power to the knight.

        :param knight: The knight to apply the weapon to.
        :type knight: Knight
        """
        knight.power += self.power


class Potion:
    """A class to represent a potion for a knight.

    :param potion: A dictionary representing the potion.
    :type potion: dict[str, str | dict[str, int | None]]
    """
    def __init__(
            self,
            potion: dict[str, str | dict[str, int | None]],
    ) -> None:
        """Initializes a Potion object.

        :param potion: A dictionary representing the potion.
        :type potion: dict[str, str | dict[str, int | None]]
        """
        self.name = potion.get("name")
        self.hp = potion.get("effect").get("hp", 0)
        self.power = potion.get("effect").get("power", 0)
        self.protection = potion.get("effect").get("protection", 0)

    def apply_potion(self, knight: "Knight") -> None:
        """Applies the potion's effects to the knight.

        :param knight: The knight to apply the potion to.
        :type knight: Knight
        """
        knight.hp += self.hp
        knight.power += self.power
        knight.protection += self.protection
