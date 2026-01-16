class Knight:
    def __init__(self, knight: dict):
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.protection = self.sum_armour(knight["armour"])
        self.power = self.sum_power(knight)
        self.apply_potion_effects(knight["potion"])

    @staticmethod
    def sum_power(knight):
        return knight["power"] + knight["weapon"]["power"]

    @staticmethod
    def sum_armour(protection):
        return sum(part["protection"] for part in protection)

    def apply_potion_effects(self, potion):
        if potion:
            self.hp += self.check_poison_effect(potion["effect"], "hp")
            self.power += self.check_poison_effect(potion["effect"], "power")
            self.protection += \
                self.check_poison_effect(potion["effect"], "protection")

    @staticmethod
    def check_poison_effect(potion_effects, effect):
        if effect in potion_effects:
            return potion_effects[effect]
        return 0
