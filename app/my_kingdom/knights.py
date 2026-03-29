class Knight:
    def __init__(self, protection,  name, power, hp, armour, weapon, potion) -> None:
        self.protection = protection
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armor else []
        self.weapon = weapon
        self.potion = potion if potion is not None else {}

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        self.hp += self.potion.get("hp", 0)
        self.power += self.potion.get("power", 0)
        self.protection += self.potion.get("protection", 0)
