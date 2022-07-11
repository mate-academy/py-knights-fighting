from protection import Protection
from power import Power
from total import Total


class TotalList:

    def __init__(self, knights: dict):
        self.knights = knights

    def battle_(self):

        knight = {}
        total_list = {}

        for people in self.knights:

            knight["protection"] = Protection.battle_protection(people)
            knight["power"] = Power.battle_power(people)
            knight["hp"] = Total.battle_hp(people)
            total_list[people] = knight

        return total_list
