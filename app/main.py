from app.battle_core.battle_preparation import TournamentPreparation
from app.battle_core.battle_preparation import Battle
from app.data.knights import KNIGHTS
from app.data.tournament_pairs import TOURNAMENT_PAIRS


def battle(knights: dict = KNIGHTS) -> dict[str, int]:
    """
    Runs a complete tournament battle simulation. Participants are prepared,
    matched into fight pairs, and each duel is executed. The final hit point
    values of all fighters are collected and returned.

     :param knights: dict with raw knight configurations, defaults to KNIGHTS
     :return: dict[str, int] - final HP values of all knights after the battle
    """
    tournament_pairs = TournamentPreparation(
        participants=knights, tournament_pairs=TOURNAMENT_PAIRS
    ).get_tournament_net()

    battle_instance = Battle(tournament_pairs=tournament_pairs)
    battle_instance.battle_start()

    return battle_instance.tournament_result()
