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
        upgrade_list_of_king["Lancelot"],
        upgrade_list_of_king["Mordred"],
    )
    result = battle_1

    # 2 Arthur vs Red Knight:
    battle_2 = Competition.battle_opponent(
        upgrade_list_of_king["Arthur"],
        upgrade_list_of_king["Red Knight"],
    )
    result.update(battle_2)

    # Result of all Battle
    result = Competition.result_of_tournament(upgrade_list_of_king)

    return result
