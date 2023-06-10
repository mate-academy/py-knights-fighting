import time

from app.knight import Knight
from my_app.prints import print_the_knight


def knights_battle(list_of_knights: list[Knight]) -> None:
    """
    This function takes 2 instances of Knight class, counts
     who is the winner(based on hp, left after battle) and returns
    string with winner's name or draw-message.
    """
    knight_1, knight_2 = list_of_knights
    print("Before the battle knights have such characteristics: ")
    for knight in list_of_knights:
        print_the_knight(knight)
    time.sleep(3)

    if knight_2.power >= knight_1.protection:
        knight_1.hp -= knight_2.power - knight_1.protection
    else:
        knight_1.protection -= knight_2.power

    if knight_1.power >= knight_2.protection:
        knight_2.hp -= knight_1.power - knight_2.protection
    else:
        knight_2.protection -= knight_1.power

    print("After the battle knights have such characteristics: ")
    for knight in list_of_knights:
        if knight.hp < 0:
            knight.hp = 0
        print_the_knight(knight)
    time.sleep(3)

    if knight_1 > knight_2:
        print(f"{knight_1.name} is winner")
    elif knight_1 < knight_2:
        print(f"{knight_2.name} is winner")
    else:
        print("Nobody wins. It is a draw")
    time.sleep(3)
