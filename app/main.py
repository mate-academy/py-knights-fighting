from app.battle.battle import Battle
from app.knights.knight_data import KNIGHTS, create_knights


def battle(all_knight: KNIGHTS) -> dict:
    knights = create_knights(all_knight)
    for knight in knights.values():
        knight.prepare_for_battle()
    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    battle1 = Battle(lancelot, mordred)
    battle1.battle_round()
    # 2 Arthur vs Red Knight:
    battle2 = Battle(arthur, red_knight)
    battle2.battle_round()
    # Return battle results:
    return {
        lancelot.name: lancelot.total_hp,
        arthur.name: arthur.total_hp,
        mordred.name: mordred.total_hp,
        red_knight.name: red_knight.total_hp,
    }


print(battle(KNIGHTS))
