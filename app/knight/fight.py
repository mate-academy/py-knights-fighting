class Battle:
    @staticmethod
    def battle(all_knights: list) -> list:
        for i in range(len(all_knights)):
            all_knights[i].hp -= (all_knights[i - 2].power
                                  - all_knights[i].protection)
            if all_knights[i].hp <= 0:
                all_knights[i].hp = 0
        return all_knights
