class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def use_weapon(self, power: int) -> None:
        self.power += power

    def use_armour(self, armour: list) -> None:
        for item in armour:
            self.hp += item["protection"]

    def use_potion(self, effects: dict) -> None:
        for key, value in effects.items():
            if key == "power":
                self.power += value
            if key == "protection":
                self.hp += value
            if key == "hp":
                self.hp += value
