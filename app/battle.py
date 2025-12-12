from app.knight import Knight


class Battle:
    knights_ = []

    @classmethod
    def check_hp(cls) -> None:
        for knight in cls.knights_:
            if knight.hp < 0:
                knight.hp = 0

    @classmethod
    def preparations(cls) -> None:
        for knight in cls.knights_:
            knight.prepare()

    @classmethod
    def one_battle(cls, name_knight1: str, name_knight2: str) -> None:
        knights = [
            knight
            for knight in cls.knights_
            if knight.name == name_knight1 or knight.name == name_knight2
        ]

        knights[0].hp -= knights[1].power - knights[0].protection
        knights[1].hp -= knights[0].power - knights[1].protection

        Battle.check_hp()

    @classmethod
    def battle(cls, knights_config: dict) -> dict:
        cls.knights_ = [
            Knight(knight)
            for knight in list(knights_config.values())
        ]
        Battle.preparations()

        # BATTLE:
        # 1 Lancelot vs Mordred:
        Battle.one_battle("Lancelot", "Mordred")

        # 2 Arthur vs Red Knight:
        Battle.one_battle("Arthur", "Red Knight")

        # Return battle results:
        return {
            cls.knights_[i].name: cls.knights_[i].hp
            for i in range(len(cls.knights_))
        }
