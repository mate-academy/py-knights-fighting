from app.knights import Knight


class Arena:

    @staticmethod
    def battle(knights: list[Knight]) -> None:
        knight1 = Knight
        knight2 = Knight
        knight3 = Knight
        knight4 = Knight
        for knight in knights:
            if knight.name == "Lancelot":
                knight1 = knight
            if knight.name == "Artur":
                knight2 = knight
            if knight.name == "Mordred":
                knight3 = knight
            if knight.name == "Red Knight":
                knight4 = knight
        knight1.hp -= knight3.power
        knight3.hp -= knight1.power
        knight2.hp -= knight4.power
        knight4.hp -= knight2.power
