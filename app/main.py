from app.Knights.knight_dict import knights_dict
from app.Battle.battle_logic import BattleLogic
from app.Knights.constructor import Knight


knights = knights_dict()


def battle(knights: dict) -> dict:
    lancelot = Knight(**knights["lancelot"])
    arthur = Knight(**knights["arthur"])
    mordred = Knight(**knights["mordred"])
    red_knight = Knight(**knights["red_knight"])

    #  1 Lancelot vs Mordred:
    first_fight = BattleLogic.battle_fight(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    second_fight = BattleLogic.battle_fight(arthur, red_knight)
    # # Return battle results:
    return {
        **first_fight,
        **second_fight
    }


print(battle(knights))
