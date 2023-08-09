from app.knights import Knight


class Arena:

    @staticmethod
    def fight(knight1: "Knight", knight2: "Knight") -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

    @staticmethod
    def check_hp(knights: list["Knight"]) -> None:
        for knight in knights:
            if knight.hp < 0:
                knight.hp = 0
