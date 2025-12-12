from app.knight import Knight


class Battle:
    @staticmethod
    def check_hp(knights: list[Knight]) -> None:
        for knight in knights:
            if knight.hp < 0:
                knight.hp = 0

    @staticmethod
    def preparations(knights_: list[Knight]) -> None:
        for knight in knights_:
            knight.prepare()

    @staticmethod
    def battle(knights_config: dict) -> dict:
        knights_ = [Knight(knight) for knight in list(knights_config.values())]
        Battle.preparations(knights_)

        # BATTLE:

        # 1 Lancelot vs Mordred:
        knights_[0].hp -= knights_[2].power - knights_[0].protection
        knights_[2].hp -= knights_[0].power - knights_[2].protection

        # 2 Arthur vs Red Knight:
        knights_[1].hp -= knights_[3].power - knights_[1].protection
        knights_[3].hp -= knights_[1].power - knights_[3].protection

        # check if someone fell in battle
        Battle.check_hp(knights_)

        # Return battle results:
        return {
            knights_[0].name: knights_[0].hp,
            knights_[1].name: knights_[1].hp,
            knights_[2].name: knights_[2].hp,
            knights_[3].name: knights_[3].hp,
        }
