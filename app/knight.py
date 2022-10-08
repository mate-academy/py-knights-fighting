class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def use_armour(self, armour: int) -> None:
        self.protection += armour.protection

    def use_weapon(self, weapon: int) -> None:
        self.power += weapon.power

    def use_potion(self, potion: int) -> None:
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]

    def battle(self, other: int) -> int:
        hp = self.hp - (other.power - self.protection)
        if hp < 0:
            hp = 0
        return hp
