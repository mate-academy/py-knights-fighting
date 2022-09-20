class Knights():

    def __init__(self, knight) -> None:
        self.name = knight["name"]
        self.power = self.knight_power(knight)
        self.hp = self.knight_hp(knight)
        self.armour = self.knight_protection(knight)

    def knight_power(self, knight):
        # calculation knight value whith potion
        return (knight["weapon"]["power"] + knight["power"] +
                self.calc_potion(knight["potion"], "power")
                )

    def knight_hp(self, knight):
        # calculation knight value whith potion
        return (knight["hp"] +
                self.calc_potion(knight["potion"], "hp")
                )

    def knight_protection(self, knight):
        # calculation knight value whith potion
        return (sum(armour["protection"] for armour in knight["armour"]) +
                self.calc_potion(knight["potion"], "protection")
                )

    @staticmethod
    def calc_potion(potion, key):
        # calculation potion value
        return (potion["effect"][key] if potion is not None and
                "effect" in potion and
                key in potion["effect"] else 0
                )

    def __sub__(self, other):
        res = self.hp - (other.power - self.armour)
        return res if res >= 0 else 0
