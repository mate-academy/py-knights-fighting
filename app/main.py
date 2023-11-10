from battle.pre_battle import pre_battle
from preparation.knights import KNIGHTS
from battle.main_battle import fighting


def battle(knightsConfig: dict) -> dict:
    lancelot, arthur, mordred, red_knight = pre_battle(knightsConfig)
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