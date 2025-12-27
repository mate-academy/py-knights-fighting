from app.knights import Knight


class Arena:
    """"Class to store functions, implementing knight's behaviour on arena"""
    @staticmethod
    def fight(knight1: "Knight", knight2: "Knight") -> None:
        """"Used formula of fighting rules"""
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

    @staticmethod
    def check_hp(knights: list["Knight"]) -> None:
        """"HP of knight must be >= 0"""
        for knight in knights:
            if knight.hp < 0:
                knight.hp = 0
