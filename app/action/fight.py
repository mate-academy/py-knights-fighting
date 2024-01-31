from app.character.knight import Knight


class Fight:
    @staticmethod
    def duel(fighter_1: Knight, fighter_2: Knight) -> None:
        hp_fighter_1 = fighter_1.hp - (fighter_2.power - fighter_1.protection)
        hp_fighter_2 = fighter_2.hp - (fighter_1.power - fighter_2.protection)
        if hp_fighter_1 <= 0:
            fighter_1.hp = 0
        else:
            fighter_1.hp = hp_fighter_1
        if hp_fighter_2 <= 0:
            fighter_2.hp = 0
        else:
            fighter_2.hp = hp_fighter_2
