from items import Armour, Potion, Weapon



class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0
        self.armours = [Armour(item) for item in knight_config["armour"]]
        self.potions = [Potion(item) for item in knight_config["potion"]]
        self.weapons = [Weapon(item) for item in knight_config["weapon"]]

    def prepare_to_battle(self) -> None:
        for armour in self.armours:
            armour.wear_armour(self)
        for potion in self.potions:
            potion.drink_potion(self)
        for weapon in self.weapons:
            weapon.wear_armour(self)
