class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self):
        total_protection = sum(part["protection"] for part in self.armour)
        self.protection = total_protection

    def apply_potion(self):
        if self.potion:
            for stat, value in self.potion["effect"].items():
                if stat == "hp":
                    self.hp += value
                elif stat == "power":
                    self.power += value
                elif stat == "protection":
                    self.protection += value

    def calculate_battle_result(self, opponent):
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp <= 0:
            self.hp = 0
        if opponent.hp <= 0:
            opponent.hp = 0
