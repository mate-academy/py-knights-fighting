class Knight:
    def __init__(self, data):
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.armour = data.get("armour")
        self.weapon = data["weapon"]
        self.potion = data.get("potion")
        self.protection = 0

    def protect(self):
        if not self.armour:
            return
        for a in self.armour:
            self.protection += a["protection"]

    def powers(self):
        self.power += self.weapon["power"]

    def potions(self):
        if not self.potion:
            return
        aaa = self.potion["effect"]
        if "protection" in aaa:
            self.protection += aaa["protection"]
        if "hp" in aaa:
            self.hp += aaa["hp"]
        if "power" in aaa:
            self.power += aaa["power"]

    def prepare(self):
        self.protect()
        self.powers()
        self.potions()

    def fight(self, enemy):
        damage = enemy.power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0