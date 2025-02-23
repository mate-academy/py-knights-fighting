from app.knights.knight_obj import Knight


class Arena:
    battle_results = {}
    knights = {}

    @staticmethod
    def fighting(knight: Knight, oponent: Knight) -> None:
        knight.hp -= oponent.power - knight.protection
        oponent.hp -= knight.power - oponent.protection

        knight.correct_stats()
        oponent.correct_stats()

        Arena.battle_results[knight.name] = knight.hp
        Arena.battle_results[oponent.name] = oponent.hp

    @staticmethod
    def knight_registration(knights: dict) -> None:
        for name, person in knights.items():
            new_knight = Knight(person)
            Arena.knights[name] = new_knight
