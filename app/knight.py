class Knight:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.protection = 0
        self.power = self.base_power

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self):
        for piece in self.armour:
            self.protection += piece.get("protection", 0)

    def apply_weapon(self):
        self.power += self.weapon.get("power", 0)

    def apply_potion(self):
        if not self.potion:
            return
        effects = self.potion.get("effect", {})
        self.hp += effects.get("hp", 0)
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)

    def attack(self, opponent: "Knight"):
        damage = self.power - opponent.protection
        opponent.hp -= max(damage, 0)
        if opponent.hp < 0:
            opponent.hp = 0
