class Character:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def use_weapon(self, power: int) -> None:
        self.power += power

    def use_armour(self, armour: list) -> None:
        if armour is not None:
            for item in armour:
                self.hp += item["protection"]

    def use_potion(self, potion: dict):
        if potion is not None:
            for key, value in potion["effect"].items():
                if key == "power":
                    self.power += value
                if key == "protection" or key == "hp":
                    self.hp += value
