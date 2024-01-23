from app.knights import Knight


class KnightFighting:

    @staticmethod
    def battle(knights: dict[object, Knight], fights: dict) -> None:
        for fighter_1, fighter_2 in fights.items():
            knights[fighter_1].hp -= (knights[fighter_2].power
                                      - knights[fighter_1].protection)
            knights[fighter_2].hp -= (knights[fighter_1].power
                                      - knights[fighter_2].protection)
            if knights[fighter_1].hp < 0:
                knights[fighter_1].hp = 0
            if knights[fighter_2].hp < 0:
                knights[fighter_2].hp = 0
