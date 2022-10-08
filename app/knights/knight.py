class Knight:
    def __init__(self, name: str, power: int, hp: int, protection: int = 0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def equip_armour(self, armour):
        self.protection += armour.protection

    def equip_weapon(self, weapon):
        self.power += weapon.power

    def equip_potion(self, potion):
        if 'power' in potion.effects:
            self.power += potion.effects['power']
        if 'hp' in potion.effects:
            self.hp += potion.effects['hp']
        if 'protection' in potion.effects:
            self.protection += potion.effects['protection']

    def battle(self, other):
        hp = self.hp - (other.power - self.protection)
        if hp < 0:
            hp = 0
        return hp
