from store.knights import KNIGHTS
from app.knights.knight import Knight
from app.battle.fight import BattleFight
from app.battle.results import get_battle_results


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights_keys = list(knights_config.keys())
    knights = []

    for key in knights_keys:
        knight = Knight(
            name=knights_config[key]["name"],
            power=knights_config[key]["power"],
            hp=knights_config[key]["hp"],
            armour=knights_config[key]["armour"],
            weapon=knights_config[key]["weapon"],
            potion=knights_config[key]["potion"]
        )
        fighter = knight.prepare_knight_to_fight()
        knights.append(fighter)

    lancelot, arthur, mordred, red_knight = knights
    # -------------------------------------------------------------------------------
    # BATTLE:
    fighters_battle = BattleFight(fighter1=lancelot, fighter2=mordred)
    fighters_battle.battle()
    lancelot, mordred = fighters_battle.get_fighters_hp()

    # 2 Arthur vs Red Knight:
    fighters_battle2 = BattleFight(fighter1=arthur, fighter2=red_knight)
    fighters_battle2.battle()
    arthur, red_knight = fighters_battle2.get_fighters_hp()

    # Return battle results:
    result = get_battle_results(lancelot, mordred, arthur, red_knight)

    return result


print(battle(KNIGHTS))
