from app.game_config import KNIGHTS, FIGHTS
from app.knights import Knight
from app.fights import FightOneToOne


def battle(knights_config):
    knights = {
        name: Knight.create_knight(information)
        for name, information in knights_config.items()
    }

    for fighter_name_1, fighter_name_2 in FIGHTS:
        single_battle = FightOneToOne(
            knight_1=knights[fighter_name_1],
            knight_2=knights[fighter_name_2]
        )
        single_battle.make_battle()

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


print(battle(KNIGHTS))
