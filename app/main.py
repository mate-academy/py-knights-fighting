from app.Knights.knight_dict import knights_dict
from app.Battle.battle_logic import BattleLogic
from app.Knights.knights_preparing import KnightPreparing


knights = knights_dict()


def battle(knights: dict) -> dict:
    lancelot = KnightPreparing(**knights["lancelot"])
    arthur = KnightPreparing(**knights["arthur"])
    mordred = KnightPreparing(**knights["mordred"])
    red_knight = KnightPreparing(**knights["red_knight"])

    # apply armour, weapon, potion if exist
    lancelot.prepare_for_fight()
    arthur.prepare_for_fight()
    mordred.prepare_for_fight()
    red_knight.prepare_for_fight()

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
