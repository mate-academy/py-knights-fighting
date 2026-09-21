from app.knight import Knight


class Fight:
    @staticmethod
    def fight(player_1: Knight, player_2: Knight) -> None:
        player_1.hp -= player_2.power - player_1.protection
        player_2.hp -= player_1.power - player_2.protection

        if player_1.hp <= 0:
            player_1.hp = 0

        if player_2.hp <= 0:
            player_2.hp = 0
