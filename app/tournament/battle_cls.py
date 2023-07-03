from time import sleep

from app.knights.knight_cls import Knight
from app.knights.knights_bases import KNIGHTS
from app.tournament.battle_funcs import Battle
from app.tournament.battle_texts import GREETING, TOURNAMENT_BEGIN, \
    REMOVED_KNIGHT, TOURNAMENT_CANCEL


class Tournament:
    def __init__(self, knights: list[Knight]) -> None:
        self.knights = knights

    def __print_knights__(self, pop_knight_name: str = "") -> None:
        for knight in self.knights:
            print(f"{knight.name}!")
            sleep(1)
        if pop_knight_name:
            print(REMOVED_KNIGHT.replace("__NAME__", pop_knight_name))

    def __knights_greetings__(self) -> bool:
        """This method print text and start others methods
        depending on different situations:
        1. Length list of Knights is not even.
        In this case lost one removed and printed info about this
        and after that started.
        2. If length is even - started.
        3. Otherwise, the method will not trigger other methods.
        """
        if len(self.knights) > 2:
            print(GREETING)
            if len(self.knights) % 2 == 1:
                knight_out = self.knights.pop(-1)
                self.__print_knights__(knight_out.name)
                print(TOURNAMENT_BEGIN)

            else:
                self.__print_knights__()
                print(TOURNAMENT_BEGIN)
            tournament_start = True
        else:
            print(TOURNAMENT_CANCEL)
            tournament_start = False
        return tournament_start

    def battle(self) -> dict:
        if self.__knights_greetings__():
            for index in range(len(self.knights) // 2):
                battle = Battle(self.knights[index],
                                self.knights[index + 2])
                battle.fight(battle_round=index + 1)
                sleep(1)
        print("The results:")
        return {
            knight.name: knight.hp
            for knight in self.knights
        }


if __name__ == "__main__":
    knights = Knight.create_knight(KNIGHTS)
    tournament = Tournament(knights=knights)
    print(tournament.battle())
