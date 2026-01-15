from app.championship_settings import KNIGHTS, BATTLE_PAIRS
from app.championship import Championship


def battle(knights_config: dict) -> dict:
    championship = Championship(knights_config, BATTLE_PAIRS)
    championship.preparation_championship()
    championship.start_championship()
    return championship.result_championship()


print(battle(KNIGHTS))
