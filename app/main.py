from app.Knights.knight_dict import knights_dict
from app.Knights.constructor import KnightConstructor
from app.Battle.battle_logic import BattleLogic


KNIGHTS = knights_dict()


def battle(KNIGHTS: dict) -> dict:
    lancelot = KnightConstructor(**KNIGHTS["lancelot"])
    arthur = KnightConstructor(**KNIGHTS["arthur"])
    mordred = KnightConstructor(**KNIGHTS["mordred"])
    red_knight = KnightConstructor(**KNIGHTS["red_knight"])

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

print(battle(KNIGHTS))







