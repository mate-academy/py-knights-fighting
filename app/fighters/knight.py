class Knight:
    def __init__(self, knight_stats):
        self.name = knight_stats["name"]
        self.power = knight_stats["power"]
        self.hp = knight_stats["hp"]
        self.armours = knight_stats["armour"]
        self.weapon = knight_stats["weapon"]
        self.potion = knight_stats["potion"]
        self.protection = 0
        self.prepare_for_battle()

    def prepare_for_battle(self):
        self.power += self.weapon["power"]

        for item in self.armours:
            self.protection += item["protection"]
        if self.potion is not None:
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)
            self.hp += self.potion["effect"].get("hp", 0)

    def fight(self, enemy):
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection
        if self.hp < 0:
            self.hp = 0
        if enemy.hp < 0:
            enemy.hp = 0
