from app.Knights.constructor import KnightConstructor


class BattleLogic(KnightConstructor):

    @staticmethod
    def battle_fight(knight1: object, knight2: object) -> dict:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        # check if someone fell in battle
        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0

        # Return battle results:
        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }