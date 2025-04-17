from app.data.knights import KNIGHTS
from app.batle_preparation.armour import BattlePreparation
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    # define objects for battle preparation
    lancelot1 = BattlePreparation(lancelot)
    arthur1 = BattlePreparation(arthur)
    mordred1 = BattlePreparation(mordred)
    red_knight1 = BattlePreparation(red_knight)

    # lancelot battle preparation
    lancelot1.apply_armour()
    lancelot1.apply_weapon()
    lancelot1.apply_potion()

    # arthur battle preparation
    arthur1.apply_armour()
    arthur1.apply_weapon()
    arthur1.apply_potion()

    # mordred battle preparation
    mordred1.apply_armour()
    mordred1.apply_weapon()
    mordred1.apply_potion()

    # red_knight battle preparation
    red_knight1.apply_armour()
    red_knight1.apply_weapon()
    red_knight1.apply_potion()

    # BATTLE:
    # 1 Lancelot vs Mordred:
    lancelot_vs_mordred = Battle(lancelot, mordred)
    lancelot_vs_mordred.battle()
    # 2 Arthur vs Red Knight:
    arthur_vs_redknight = Battle(arthur, red_knight)
    arthur_vs_redknight.battle()

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
