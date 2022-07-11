class Protection:

    def __init__(self, knight: dict):
        self.knight = knight

    def battle_protection(self):
        self.knight["protection"] = 0
        for a in self.knight["armour"]:
            self.knight["protection"] += a["protection"]  # 0
        if self.knight["potion"] is not None:
            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += self.knight["potion"]["effect"]["protection"]
        return self.knight["protection"]


# BATTLE PREPARATIONS:
# Подготовка к бою
# protection - защита   armour - броня