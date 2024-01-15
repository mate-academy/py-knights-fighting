from ..knight.knight import Knight


class Contest:

    def __init__(self) -> None:
        self.ritters = list()
        print("Welcome to contest!")

    def create_knight_instances(self, knights: dict) -> None:

        for ritter in knights:
            self.ritters.append(Knight(**knights[ritter]))

    def prepare_for_battle(self) -> None:

        for ritter in self.ritters:
            ritter.prepare_for_battle()

    @staticmethod
    def check_hp(knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0
            print(f"{knight.name} is dead")

    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        if knight_1.hp <= 0:
            knight_1.hp = 0
            print(f"{knight_1.name} is dead")

    def start_battles(self) -> None:
        print("!!!BATTLE!!!")
        for index in range(len(self.ritters) // 2):
            self.fight(self.ritters[index], self.ritters[index + 2])
            self.fight(self.ritters[index + 2], self.ritters[index])

        print("All fights are completed!")

    def get_contest_results(self) -> dict:
        contest_results = dict()

        for knight in self.ritters:
            contest_results[knight.name] = knight.hp

        return contest_results
