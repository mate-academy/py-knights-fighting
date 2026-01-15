from app.knights.knight import Knight


class Camelot:

    def __init__(self) -> None:
        pass

    @classmethod
    def knight_battle(cls, knight_one: Knight, knight_two: Knight) -> dict:
        knight_one.hp -= knight_two.power - knight_one.protection
        knight_two.hp -= knight_one.power - knight_two.protection

        knight_one.hp = max(knight_one.hp, 0)
        if knight_one.hp == 0:
            print(f"{knight_one.name} fall in battle!")

        knight_two.hp = max(knight_two.hp, 0)
        if knight_two.hp == 0:
            print(f"{knight_two.name} fall in battle!")

        return {
            knight_one.name : knight_one.hp,
            knight_two.name : knight_two.hp
        }
