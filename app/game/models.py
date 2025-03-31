class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list["Armour"] | None = None,
            weapon: "Weapon" | None = None,
            potion: "Potion" | None = None,
    ) -> None:
        """
        Initializes a Knight with the ability to calculate final stats based on provided items.

        Args:
            name (str): The name of the knight.
            power (int): The base attack power of the knight.
            hp (int): The base health points of the knight.
            armour (list[Armour] | None, optional): A list of armour parts providing protection. Defaults to None.
            weapon (Weapon | None, optional): The knight's weapon which adds to power. Defaults to None.
            potion (Potion | None, optional): A potion that temporarily boosts stats. Defaults to None.
        """
        self.name: str = name
        self.base_power: int = power
        self.base_hp: int = hp
        self.armour: list["Armour"] = armour or []
        self.weapon: "Weapon" | None = weapon
        self.potion: "Potion" | None = potion
        self.calculate_final_stats()

    def calculate_final_stats(self) -> None:
        """Calculates and updates the final stats of the knight based on provided items."""
        self.protection: int = sum(part.protection for part in self.armour)
        self.power: int = self.base_power + (self.weapon.power if self.weapon else 0)
        self.hp: int = self.base_hp
        if self.potion:
            potion_effects: dict[str, int] = self.potion.effect
            self.hp += potion_effects.get("hp", 0)
            self.power += potion_effects.get("power", 0)
            self.protection += potion_effects.get("protection", 0)


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        """
        Initializes a Weapon.

        Args:
            name (str): The name of the weapon.
            power (int): The additional attack power provided by the weapon.
        """
        self.name: str = name
        self.power: int = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        """
        Initializes a piece of Armour.

        Args:
            part (str): The part of the body the armour is for.
            protection (int): The protection value the armour provides.
        """
        self.part: str = part
        self.protection: int = protection


class Potion:
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        """
        Initializes a Potion.

        Args:
            name (str): The name of the potion.
            effect (dict[str, int]): A dictionary of stat boosts the potion provides.
                                        Keys may include "hp", "power", and "protection".
        """
        self.name: str = name
        self.effect: dict[str, int] = effect