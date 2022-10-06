from app.battle_begin.result import Result


class Logic:
    @staticmethod
    def ready_set_go(knights):
        knights = [value for key, value in knights.items()]
        for i in range(len(knights) - 2):
            knights[i].hp -= knights[i + 2].power - knights[i].protection
            knights[i + 2].hp -= knights[i].power - knights[i + 2].protection
            if knights[i].hp <= 0:
                knights[i].hp = 0
            if knights[i + 2].hp <= 0:
                knights[i + 2].hp = 0

        result_battle = Result()
        result_battle.show_result(knights)
