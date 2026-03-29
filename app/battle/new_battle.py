class Battle:

    @staticmethod
    def knight_battle(knight1, knight2):
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0

        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }
