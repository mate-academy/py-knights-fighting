class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list) -> int:
        for part in armour:
            self.protection += part["protection"]
        return self.protection

    def apply_weapon(self, weapon: dict) -> int:
        self.power += weapon["power"]
        return self.power

    def apply_potion(self, potion: dict) -> None:
        if potion:
            potion_effect = potion["effect"]
            for key in potion_effect:
                if key == "hp":
                    self.hp += potion_effect["hp"]
                if key == "power":
                    self.power += potion_effect["power"]
                if key == "protection":
                    self.protection += potion_effect["protection"]
