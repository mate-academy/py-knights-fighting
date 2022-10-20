class Warrior:
    """
    The class based on which the heroes will be created
    """
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list) -> int:
        """
        Method for pumping protection

        In this method, we pump the character's protection property
        :param armour: list
        :return: int
        """
        if armour is not None:
            for arm in armour:
                self.protection += arm["protection"]
            return self.protection

        return self.protection

    def apply_weapon(self, weapon: dict) -> int:
        """
        Method for pumping power

        In this method, we are pumping the character's power property
        :param weapon: dict
        :return: int
        """
        if weapon is not None:
            for i in range(len(weapon) - 1):
                self.power += weapon["power"]
            return self.power

        return self.power

    def apply_potion(self, potion: dict) -> object:
        """
        Applying potions to a character

        In this method, we level the character by referring to his potions.
        :param potion: dict
        :return: self
        """
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]

        return self
