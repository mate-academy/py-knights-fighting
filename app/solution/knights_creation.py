class Knights:

    def __init__(self, name, power, hp, protection):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def one_battle(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
        return {self.name: self.hp, other.name: other.hp}
