class Knight:
    """
    A class representing a knight with attributes such as name, power,
    hp (health points), armour, weapon, and potion.

    Attributes:
        name (str): The name of the knight.
        base_power (int): The base attack power of the knight.
        hp (int): The health points of the knight.
        armour (list[dict]): A list of armour pieces, each represented as a
                             dictionary containing part and protection.
        weapon (dict): A dictionary representing the weapon, containing its
                       name and power.
        potion (dict, optional): A dictionary representing a potion,
                                 containing its name and effects on the
                                 knight's stats.

    Methods:
        apply_armour(): Applies the total protection from the knight's armour.
        apply_weapon(): Adds the weapon power to the knight's total power.
        apply_potion(): Applies the effects of the potion (if any) to the
                        knight's stats.
        take_damage(damage: int): Reduces the knight's hp by the given damage,
                                  considering the knight's protection.
        calculate_stats(): Calculates the knight's final stats by applying
                           their armour, weapon, and potion effects.
    """
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.total_power = 0

    def apply_armour(self) -> None:
        self.protection = sum(
            armour_element["protection"]
            for armour_element in self.armour
        )

    def apply_weapon(self) -> None:
        self.total_power = self.base_power + self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion["effect"].items():
                match stat:
                    case "hp":
                        self.hp += value
                    case "power":
                        self.total_power += value
                    case "protection":
                        self.protection += value

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def calculate_stats(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
