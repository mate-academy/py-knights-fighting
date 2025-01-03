class Knight:
    def __init__(self, name: str, power: int,
                 hp: int,
                 weapon: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.power += self.weapon
        self.armour = None

    def apply_armour(self, protection: list[dict]) -> None:
        result = 0
        if len(protection) == 0:
            self.armour = 0
        for armour in protection:
            result += armour["protection"]
        self.armour = result

    def apply_potion(self, potion: dict) -> None:
        for key, value in potion.items():
            if str(value).strip("+-").isnumeric():
                if key == "hp":
                    self.hp += value
                elif key == "power":
                    self.power += value
                elif key == "protection":
                    self.armour += value
