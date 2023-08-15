class Battle:
    @staticmethod
    def battle(all_kn: list) -> list:
        for i in range(4):
            all_kn[i].hp -= all_kn[i - 2].power - all_kn[i].protection
            if all_kn[i].hp <= 0:
                all_kn[i].hp = 0
        return all_kn
