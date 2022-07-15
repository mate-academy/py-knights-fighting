from .protection import Protection
from .power import Power
from .total import Total
from app.battle_knights.knights_dict import knights


class TotalList:

    def __init__(self, person=knights):
        self.person = person

    def battle_(self):
        total_dict = {}
        for knight_per, people_k in self.person.items():
            prot = Protection(knight_p=people_k)
            a = prot.battle_protection()
            power_p = Power(knight_people=people_k)
            b = power_p.battle_power()
            total_t = Total(knight_person=people_k)
            c = total_t.battle_hp()
            knight = a | b | c
            total_dict[knight_per] = knight
        return total_dict
