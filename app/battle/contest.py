from ..knight.knight import Knight


class Contest:
    def __init__(self) -> None:
        print("Welcome to contest!")

    @staticmethod
    def create_knight_instances(ritters: dict) -> list:
        knight_instances = list()

        for ritter in ritters:
            knight_instances.append(Knight(
                ritters[ritter]["name"],
                ritters[ritter]["power"],
                ritters[ritter]["hp"],
                ritters[ritter]["armour"],
                ritters[ritter]["weapon"],
                ritters[ritter]["potion"]
            ))

        return knight_instances

    @staticmethod
    def prepare_for_battle(ritters: list) -> None:

        for ritter in ritters:
            ritter.prepare_for_battle()

    @classmethod
    def fight(cls, knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        if knight_1.hp <= 0:
            knight_1.hp = 0

        if knight_2.hp <= 0:
            knight_2.hp = 0

    @classmethod
    def start_battles(cls, ritters: list) -> None:
        print("!!!BATTLE!!!")
        for index in range(0, len(ritters) // 2):
            cls.fight(ritters[index], ritters[index + 2])

        print("All fights are completed!")

    @staticmethod
    def get_contest_results(knights: list) -> dict:
        contest_results = dict()

        for knight in knights:
            contest_results[knight.name] = knight.hp

        return contest_results
