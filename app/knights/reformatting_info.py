from app.knights.class_knight import Knight

"""

This func is created for reformatting information
about the Knights from dict type to class type

"""


def making_knight(knight: dict) -> Knight:
    knight_adj = Knight(

        name=knight["name"],
        power=knight["power"],
        hp=knight["hp"],
        armour=knight["armour"],
        weapon=knight["weapon"],
        potion=knight["potion"],

    )

    knight_adj.using_potion()

    return knight_adj
