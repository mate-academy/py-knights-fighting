from .total_list import TotalList
from app.battle_knights.knights_dict import knights


class BattleF:

    def __init__(self, knights_d=knights):
        self.knights_d = knights_d

    def total_hp(self):
        total = {}
        total_l = TotalList(person=self.knights_d)
        total_list = total_l.battle_()
        total_list["lancelot"]["hp"] -=\
            total_list["mordred"]["power"] -\
            total_list["lancelot"]["protection"]
        total["lancelot"] = total_list["lancelot"]["hp"]
        total_list["mordred"]["hp"] -=\
            total_list["lancelot"]["power"] -\
            total_list["mordred"]["protection"]
        total["mordred"] = total_list["mordred"]["hp"]
        total_list["arthur"]["hp"] -=\
            total_list["red_knight"]["power"] -\
            total_list["arthur"]["protection"]
        total["arthur"] = total_list["arthur"]["hp"]
        total_list["red_knight"]["hp"] -=\
            total_list["arthur"]["power"] -\
            total_list["red_knight"]["protection"]
        total["red_knight"] = total_list["red_knight"]["hp"]
        return total
