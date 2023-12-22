from app.kings.kings_init import KingsConfigur
from app.battle_resurlt.battle_resullt import Competition


def battle(list_king: dict) -> dict:
    # Introduce the list of kings
    list_of_king = KingsConfigur(list_king)
    # Upgrade with configurations
    upgrade_list_of_king = KingsConfigur.configure(list_of_king)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle_1 = Competition.battle_opponent(
        "Lancelot",
        "Mordred",
        upgrade_list_of_king
    )
    upgrade_list_of_king = battle_1

    # 2 Arthur vs Red Knight:
    battle_1 = Competition.battle_opponent(
        "Arthur",
        "Red Knight",
        upgrade_list_of_king
    )
    upgrade_list_of_king = battle_1

    # Result of all Battle
    result = Competition.result_of_tournament(upgrade_list_of_king)

    return result
