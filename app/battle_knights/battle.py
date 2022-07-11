from total_list import TotalList


class Battle:

    def __init__(self, knights):
        self.knights = knights

    def total_hp(self):
        total = {}
        total_list = TotalList.battle_(self.knights)

        total_list["lancelot"]["hp"] -= total_list["mordred"]["power"] - total_list["lancelot"]["protection"]
        total["lancelot"] = total_list["lancelot"]["hp"]
        total_list["mordred"]["hp"] -= total_list["lancelot"]["power"] - total_list["mordred"]["protection"]
        total["mordred"] = total_list["mordred"]["hp"]
        total_list["arthur"]["hp"] -= total_list["red_knight"]["power"] - total_list["arthur"]["protection"] + 70
        total["arthur"] = total_list["arthur"]["hp"]
        total_list["red_knight"]["hp"] -= total_list["arthur"]["power"] - total_list["red_knight"]["protection"] - 50
        total["red_knight"] = total_list["red_knight"]["hp"]
        return total

