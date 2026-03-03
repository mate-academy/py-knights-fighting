class Knight:
    """
    Represents a medieval knight with combat statistics.

    Calculate effective health, power and protection by
    considering base stats, equiped gear and consumed potions.
    """
    def __init__(self, knight_data: dict) -> None:
        """
        Initialize a Knight instance from a data dictionary.

        Args:
            knight_data: A dictionary containing knight's name,
                         hp, power, armour, weapon and potion.
        """
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.protection = 0

        for item in knight_data["armour"]:
            self.protection += item["protection"]

        self.power += knight_data["weapon"]["power"]

        potion = knight_data["potion"]
        if potion:
            effect = potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
