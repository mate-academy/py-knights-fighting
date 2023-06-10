from app.knight import Knight
from app.data import KNIGHTS
from my_app.knights_battle import knights_battle

from my_app.random_knight import random_knight


def main() -> None:
    """
    To know who will win the battle of two knights, please, choose knights.
    To choose, input knight's number below.

    If You want to play with existed knights press 1
    If You want to use random knights press 2
    Exit - press q

    If You choose game with existed knights, choose knight, please:
        Lancelot = 0
        Arthur = 1
        Mordred = 2
        Red knight = 3

    The winner is knight that has more hp after battle
    """
    while True:
        print("""
        If You want to play with existed knights press 1
        If You want to use random knights press 2
        Exit - press q
        """)
        choice = input("Make Your choice, please: ")
        if choice == "1":
            print("""
                To choose Your knights input number from 0 to 3.
                Lancelot = 0
                Arthur = 1
                Mordred = 2
                Red knight = 3
                """)
            list_of_knights = exists_knights(KNIGHTS)
            knights_battle(list_of_knights=list_of_knights)

        elif choice == "2":
            knight_1 = random_knight()
            knight_2 = random_knight()
            list_of_knights = [knight_1, knight_2]
            knights_battle(list_of_knights=list_of_knights)
        elif choice == "q":
            break
        else:
            print("Make correct choice, please")


def exists_knights(knights_config: dict) -> list[Knight]:
    """
    This function makes You to choose 2 of exist knights and return
    list of Knight class instances
    """
    index_1 = int(input("Choose first knight: "))
    index_2 = int(input("Choose second knight: "))

    list_of_knights = Knight.creation(knights_config=knights_config)
    knight_1 = list_of_knights[index_1]
    knight_2 = list_of_knights[index_2]
    return [knight_1, knight_2]


if __name__ == "__main__":
    main()
