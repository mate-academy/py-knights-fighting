def simulate_battle(first_participant: str,
                    second_participant: str,
                    participant_stats: dict) -> dict:
    first_participant_hp = (
        participant_stats)[first_participant]["hp"]
    first_participant_power = (
        participant_stats)[first_participant]["power"]
    first_participant_protection = (
        participant_stats)[first_participant]["protection"]
    second_participant_hp = (
        participant_stats)[second_participant]["hp"]
    second_participant_power = (
        participant_stats)[second_participant]["power"]
    second_participant_protection = (
        participant_stats)[second_participant]["protection"]
    first_participant_hp -= (second_participant_power -
                             first_participant_protection)
    second_participant_hp -= (first_participant_power -
                              second_participant_protection)
    result = {participant_stats[first_participant]["knight_name"]:
                  if_less_zero(first_participant_hp),
              participant_stats[second_participant]["knight_name"]:
                if_less_zero(second_participant_hp)}
    return result


def if_less_zero(hp: int) -> int:
    return 0 if hp <= 0 else hp
