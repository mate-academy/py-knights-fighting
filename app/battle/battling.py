from app.character.knight import Knight


class BattleArea:
    @staticmethod
    def dual_hit(k1: Knight, k2: Knight) -> None:
        # hit to k1
        hit = k2.power - k1.protection
        if hit >= 0:
            k1.hp -= hit
        if k1.hp < 0:
            k1.hp = 0
            print(f"{k1.name} died!")
        print(f"{k2.name} hit {k1.name}")

        # hit to k2
        hit = k1.power - k2.protection

        if hit >= 0:
            k2.hp -= hit
        if k2.hp < 0:
            k2.hp = 0
            print(f"{k2.name} died!")
        print(f"{k1.name} hit {k2.name}")

    @staticmethod
    def duel(k1: Knight, k2: Knight) -> None:
        while k1.hp != 0 or k2.hp != 0:
            BattleArea.dual_hit(k1, k2)
