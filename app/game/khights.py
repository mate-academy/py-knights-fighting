class Knight:
    def __init__(self, name, power, hp, armour=None, weapon=None, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon if weapon is not None else {}
        self.potion = potion if potion is not None else {}
        self.armour = armour if armour is not None else []

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def calculate_total_protection(self):
        total_protection = sum(armour.protection for armour in self.armour)
        if self.potion is not None and "effect" in self.potion \
                and "protection" in \
                self.potion["effect"]:
            total_protection += self.potion["effect"]["protection"]

        return total_protection

    def battle(self, opponent):
        damage_to_opponent = max(0, self.power -
                                 opponent.calculate_total_protection())
        damage_to_self = max(0, opponent.power -
                             self.calculate_total_protection())
        self.hp -= damage_to_self
        opponent.hp -= damage_to_opponent

        result = f"{self.name} dealt {damage_to_opponent} damage to " \
                 f"{opponent.name} and received {damage_to_self} damage"
        if self.hp <= 0:
            result += f"\n{self.name} has been defeated"
        if opponent.hp <= 0:
            result += f"\n{opponent.name} has been defeated"

        return result


class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection
