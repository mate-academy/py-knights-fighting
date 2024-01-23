from app.knights import Knight


class KnightFighting:

    @staticmethod
    def battle(knights: dict[object, Knight], fights: dict) -> None:
        for fighter_1, fighter_2 in fights.items():
            fighter_1 = knights[fighter_1]
            fighter_2 = knights[fighter_2]
            fighter_1.hp -= (fighter_2.power - fighter_1.protection)
            fighter_2.hp -= (fighter_1.power - fighter_2.protection)
            if fighter_1.hp < 0:
                fighter_1.hp = 0
            if fighter_2.hp < 0:
                fighter_2.hp = 0
