from data.knights import KNIGHTS


class Knight():
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __str__(self):
        return f"Knight {self.name} (Power: {self.power}, HP: {self.hp})"

arthur = Knight(**KNIGHTS["arthur"])
print("Лицар створений напряму:")
print(arthur)
