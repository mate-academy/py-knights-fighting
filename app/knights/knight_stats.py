class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = sum(item["protection"] for item in armour)
        if potion:
            self.hp += potion["effect"].get("hp", 0)
            self.power += potion["effect"].get("power", 0)
            self.protection += potion["effect"].get("protection", 0)

    def calculate_damage(self, opponent):
        return max(0, self.power - opponent.protection)
