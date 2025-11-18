class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armor: list, weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion

    def batle_preparation(self):
        self.protection = 0
        for piece in self.armor:
            self.protection += piece.protection

        self.power += self.weapon.power

        if self.potion is not None:
            effects = self.potion.effects
            if "power" in effects:
                self.power += effects["power"]

            if "protection" in effects:
                self.protection += effects["protection"]

            if "hp" in effects:
                self.hp += effects["hp"]


arthur = Knight("Arthur", 45, 75,
                    [arthur_helmet, arthur_breastplate, arthur_boots],
                    th_sword, None)