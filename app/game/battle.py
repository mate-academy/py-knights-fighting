from app.game.knight import Knight


class Battle:
    @classmethod
    def _get_result(cls, player_1: Knight, player_2: Knight) -> dict:
        return {player_1.name: player_1.hp,
                player_2.name: player_2.hp}

    @classmethod
    def _get_start_player_to_battle(cls, player_1: Knight, player_2: Knight) -> None:
        player_1.start_to_battle()
        player_2.start_to_battle()

    @staticmethod
    def start_battle(player_1: Knight, player_2: Knight) -> dict:
        Battle._get_start_player_to_battle(player_1, player_2)
        print(f"Player_1: {player_1}")
        print(f"Player_2: {player_2}")

        player_1.hp -= player_2.power - player_1.protection
        player_2.hp -= player_1.power - player_2.protection

        if player_1.hp <= 0:
            player_1.hp = 0

        if player_2.hp <= 0:
            player_2.hp = 0

        return Battle._get_result(player_1, player_2)
