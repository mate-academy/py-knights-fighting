class Knight:

    def __init__(self, name: str, power: int, hp: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = []

    def check_look(self):
        print(f"Name: {self.name}, "
              f"Power: {self.power}, "
              f"Hp: {self.hp}, "
              f"Protection: {self.protection}, "
              f"Armour: {self.armour}, "
              f"Weapon: {self.weapon}, "
              f"Potion: {self.potion}")

    def __str__(self):
        return f"{self.name}"

    def put_on_armour(self, armour):
        self.armour.append(armour)
        self.protection += armour.protection

    def take_weapon(self, weapon):
        self.weapon = weapon
        self.power += weapon.power

    def take_potion(self, potion):
        self.potion.append(potion)
        self.protection += potion.protection
        self.power += potion.power
        self.hp += potion.hp
