class Logic:
    def ready_set_go(self, knights):
        print(list(knights))
        knights = [value for key, value in knights.items()]
        print(knights)
        for i in range(len(knights) - 2):
            knights[i].hp -= knights[i + 2].power - knights[i].protection
            knights[i + 2].hp -= knights[i].power - knights[i + 2].protection
            if knights[i].hp <= 0:
                knights[i].hp = 0
            if knights[i + 2].hp <= 0:
                knights[i + 2].hp = 0

            # knights['lancelot'].hp -= knight['mordred'].power - knight['lancelot'].lancelot

        # lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        #     mordred["hp"] -= lancelot["power"] - mordred["protection"]
