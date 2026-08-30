class Knight:
    def __init__(self, name, power, hp, armour=None, weapon=None, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon or {}
        self.potion = potion
        self.protection = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


