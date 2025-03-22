

class Power:

    def __init__(self, armour: list, weapon: dict, potion: dict) -> None:
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def total_power(self) -> tuple:
        sum_power = 0
        sum_protection = 0
        sum_hp = 0
        sum_protection = sum([arm.get("protection", 0) for arm in self.armour])
        if self.weapon:
            sum_power += self.weapon.get("power", 0)
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            sum_power += effect.get("power", 0)
            sum_protection += effect.get("protection", 0)
            sum_hp += effect.get("hp", 0)

        return sum_hp, sum_power, sum_protection
