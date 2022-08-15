from app.knights.knight import Knight
from app.battle.battle import battle_round
from app.battle.preparation import preparing_for_battle
from app.battle.current_stats import current_stats


def battle(knights):

    lancelot, arthur, mordred, red_knight = [

        Knight(name=knights[person]["name"],
               power=knights[person]["power"],
               hp=knights[person]["hp"],
               weapon=knights[person]["weapon"],
               armour=knights[person]["armour"],
               potion=knights[person]["potion"],
               protection=0)
        for person in knights
    ]

    preparing_for_battle()

    battle_round(lancelot, mordred)
    battle_round(arthur, red_knight)

    return current_stats()
