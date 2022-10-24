from app.knights.knight import Knight


class Fight:
    @staticmethod
    def hit(knight_1: Knight, knight_2: Knight) -> None:
        # knight_1 damage
        damage = knight_1.power - knight_2.protection
        if damage >= 0:
            knight_2.hp -= damage
        if knight_2.hp <= 0:
            knight_2.hp = 0
            knight_2.died = True
            print(f"{knight_2.name} is died!")
        print(f"{knight_1.name} hit {knight_2.name}!")

        # knight_2 damage
        damage = knight_2.power - knight_1.protection
        if damage > 0:
            knight_1.hp -= damage
        if knight_1.hp <= 0:
            knight_1.hp = 0
            knight_1.died = True
            print(f"{knight_1.name} is died!")
        print(f"{knight_2.name} hit {knight_1.name}!")

    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        while not any([knight_1.died, knight_2.died]):
            Fight.hit(knight_1, knight_2)
