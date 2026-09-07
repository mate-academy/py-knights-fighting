from app.knights import knights_list

class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: dict, potion: dict | None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def arm_knight(self):

        if self.armour:
            for piece in self.armour:
                self.protection += piece["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            hp = self.potion.get("hp")
            protection = self.potion.get("protection")
            power = self.potion.get("power")

            if hp :
                self.hp += hp
            if protection:
                self.protection += protection
            if power:
                self.power += power

knights = {name:Knight(knight["name"], knight["power"], knight["hp"],
                  knight["armour"], knight["weapon"], knight["potion"])
           for name, knight in knights_list.KNIGHTS.items()}
for value in knights.values():
    print(value.__dict__)