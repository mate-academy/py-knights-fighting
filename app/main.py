from action.action import Action
from data.custom_data import KNIGHTS


def battle(knights: dict) -> dict:

    list_of_knights = Action.create_knight(knights)

    Action.apply_armour(list_of_knights)
    Action.apply_potion(list_of_knights)
    Action.apply_weapon(list_of_knights)

    max = len(list_of_knights)
    full = max - (max % 4)
    chunk = list(range(full, max))

    for i in range(0, full, 4):
        for j in range(i, i + 2, 1):
            print(f"{j} vs {j + 2}")
            Action.knight_fight(list_of_knights[j], list_of_knights[j + 2])


    if chunk:
        if len(chunk) == 3:
            print(f"{chunk[0]} vs {chunk[2]}")
            Action.knight_fight(list_of_knights[chunk[0]], list_of_knights[chunk[2]])
            print(f"Knight {list_of_knights[chunk[1]].name}: {chunk[1]} dont have an opponent")
        elif len(chunk) == 2:
            print(f"{chunk[0]} vs {chunk[1]}")
            Action.knight_fight(list_of_knights[chunk[0]], list_of_knights[chunk[1]])
        else:
            print(f"Knight {list_of_knights[chunk[0]].name}: {chunk[0]} dont have an opponent")

    return {
        knight.name: knight.hp for knight in list_of_knights
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
