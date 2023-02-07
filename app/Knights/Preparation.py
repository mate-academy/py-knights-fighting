class Prepare:
    knights_dict = {}

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = 0

    def protection_update(self, armours: list) -> None:
        for armour in armours:
            self.armour += armour["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                self.armour += potion["effect"]["protection"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]

    def update(self, armour: list, weapon: dict, potion: dict) -> None:
        self.protection_update(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)
