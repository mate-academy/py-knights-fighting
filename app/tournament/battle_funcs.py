from time import sleep

from app.knights.knight_cls import Knight


class Battle:
    def __init__(self,
                 first_fighter: Knight,
                 second_fighter: Knight):
        self.fighter1 = first_fighter
        self.fighter2 = second_fighter
        self.fighters = [first_fighter, second_fighter]

    @staticmethod
    def __fight_hp__(first: Knight, second: Knight) -> Knight:
        first.hp -= second.power - first.protection
        first.hp = 0 if first.hp < 0 else first.hp
        if not first.hp:
            print(f"Sir {first.name} was killed in this duel.")
        return first

    @staticmethod
    def __winner__(first: Knight, second: Knight) -> None:
        winner = " is winner!"
        print(
            "They look equally beaten, there is no winner!"
            if first.hp == second.hp
            else first.name + winner if first.hp > second.hp
            else second.name + winner
        )

    def fight(self, battle_round: int) -> None:
        print(f"Round {battle_round}")
        print(f"In left side - {self.fighter1.name}, "
              f"opposite - {self.fighter2.name}.")
        for index, fighter in enumerate(self.fighters):
            self.__fight_hp__(self.fighters[index],
                              self.fighters[index - 1])

        sleep(1)
        self.__winner__(self.fighter1, self.fighter2)
        sleep(1)
