class KnightBattle:
    @staticmethod
    def battle(knight1, knight2):
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        # return knight1["hp"], knight2["hp"]

    @staticmethod
    def chek_hp(knight1, knight2, knight3, knight4):
        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0
        if knight3.hp <= 0:
            knight3.hp = 0
        if knight4.hp <= 0:
            knight4.hp = 0
        # return knight1["hp"], knight2["hp"],knight3["hp"], knight4["hp"]


