from .protection import Protection
from .power import Power
from .total import Total
from app.battle_knights.knights_dict import knights


class TotalList:

    def __init__(self, person=knights):
        self.person = person

    def battle_(self):
        knight = {}
        total_dict = {}
        protect = Protection(people_dict=self.person)
        knight["protection"] = protect.battle_protection()
        power_p = Power(knights_person=self.person)
        knight["power"] = power_p.battle_power()
        total_t = Total(dict_knights=self.person)
        knight["hp"] = total_t.battle_hp()
        for people_k in self.person:
            total_dict[people_k] = knight
        return total_dict
