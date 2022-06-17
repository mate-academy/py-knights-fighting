class Knight:

    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.profit_from_armour()
        self.profit_from_weapon()
        self.profit_from_poison()

    def profit_from_armour(self):
        for prot in self.armour:
            self.protection += prot["protection"]

    def profit_from_weapon(self):
        self.power += self.weapon['power']

    def profit_from_poison(self):
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def death_check(self):
        if self.hp < 0:
            self.hp = 0

    def battle_knights(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        # health check
        self.death_check()
        other.death_check()

    @staticmethod
    def from_dict_to_class(knights):
        res = {}
        for knight in knights:
            stats = [knights[knight][x] for x in list(knights[knight])]
            res[knight] = Knight(*stats)
        return res
