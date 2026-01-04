from app.init_battle.pre_battle import pre_battle
from app.preparation.knights import KNIGHTS
from app.init_battle.main_battle import fighting


def battle(knights: dict) -> dict:
    lancelot, arthur, mordred, red_knight = pre_battle(knights)
    fighting(lancelot, mordred)
    fighting(arthur, red_knight)

    return {
        lancelot.name : lancelot.hp,
        arthur.name : arthur.hp,
        mordred.name : mordred.hp,
        red_knight.name: red_knight.hp
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
