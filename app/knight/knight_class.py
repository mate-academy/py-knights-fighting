from __future__ import annotations


class Knight:
    """
    Create Knight class instance and store its attributes.
    """
    all_knights = dict()

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        Knight.all_knights[self.name] = self.apply_knight_attributes(self)

    @staticmethod
    def apply_knight_attributes(knight: Knight) -> Knight:
        """
        Apply knight's extra attributes to main ones (e.g. hp, power).
        :param: knight:
        :return: Knight instance
        """
        # apply armour
        knight.protection = 0
        for armour in knight.armour:
            knight.protection += armour["protection"]

        # apply weapon
        knight.power += knight.weapon["power"]

        # apply potion if it exists
        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]

            if "protection" in knight.potion["effect"]:
                knight.protection += knight.potion["effect"]["protection"]

            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
        return knight

    @staticmethod
    def get_knights(knights_config: dict) -> dict:
        """
        Create Knight instances, apply their additional attributes and store.
        :param: knights_config:
        :return: a dictionary of Knight instances
        """
        for knight_config in knights_config.values():
            Knight(**knight_config)
        return Knight.all_knights

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__} class, "
                f"name: {self.name}, "
                f"power: {self.power}, "
                f"hp: {self.hp}, "
                f"weapon: {self.weapon}, "
                f"armour: {self.armour},"
                f"potion: {self.potion},"
                f"protection: {self.protection}")
