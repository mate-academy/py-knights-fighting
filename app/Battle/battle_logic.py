class BattleLogic:

    @staticmethod
    def battle_fight(knight1: object, knight2: object) -> dict:
        # fight and check if someone fell in battle
        knight1.hp = max(knight1.hp - (knight2.power - knight1.protection), 0)
        knight2.hp = max(knight2.hp - (knight1.power - knight2.protection), 0)

        # Return battle results:
        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }
