from app.kings.kings_init import KingsConfigur
from app.battle_resurlt.battle_resullt import Battle
from app.battle_resurlt.win import Win


def battle(list_king: dict) -> dict:
    # Introduce the list of kings
    list_of_king = KingsConfigur(list_king)
    # Upgrade with configurations
    upgrade_list_of_king = KingsConfigur.configure(list_of_king)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle_1 = Battle("Lancelot", "Mordred", upgrade_list_of_king)
    upgrade_list_of_king = battle_1.battle_opponent()

    # 2 Arthur vs Red Knight:
    battle_1 = Battle("Arthur", "Red Knight", upgrade_list_of_king)
    upgrade_list_of_king = battle_1.battle_opponent()

    # Result of all Battle
    result = Win.result_of_tournament(upgrade_list_of_king)

    return result
