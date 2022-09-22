from app.character.knight import Knight


class BattleArea:
    @staticmethod
    def dual_hit(knight1: Knight, knight2: Knight) -> None:
        # hit to knight1
        hit = knight2.power - knight1.protection
        if hit >= 0:
            knight1.hp -= hit
        if knight1.hp < 0:
            knight1.hp = 0
            print(f"{knight1.name} died!")
        print(f"{knight2.name} hit {knight1.name}")

        # hit to knight2
        hit = knight1.power - knight2.protection

        if hit >= 0:
            knight2.hp -= hit
        if knight2.hp < 0:
            knight2.hp = 0
            print(f"{knight2.name} died!")
        print(f"{knight1.name} hit {knight2.name}")

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> None:
        while knight1.hp != 0 or knight2.hp != 0:
            BattleArea.dual_hit(knight1, knight2)
