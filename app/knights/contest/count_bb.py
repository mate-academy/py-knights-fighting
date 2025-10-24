def calculation_before_battle(first_participant: str,
                              second_participant: str,
                              list_participants: dict) -> dict:
    first_participant_hp = (
        list_participants)[first_participant]["hp"]
    first_participant_power = (
        list_participants)[first_participant]["power"]
    first_participant_protection = (
        list_participants)[first_participant]["protection"]
    second_participant_hp = (
        list_participants)[second_participant]["hp"]
    second_participant_power = (
        list_participants)[second_participant]["power"]
    second_participant_protection = (
        list_participants)[second_participant]["protection"]
    first_participant_hp -= (second_participant_power -
                             first_participant_protection)
    second_participant_hp -= (first_participant_power -
                              second_participant_protection)
    result = {list_participants[first_participant]["knight_name"]:
                  if_less_zero(first_participant_hp),
              list_participants[second_participant]["knight_name"]:
                if_less_zero(second_participant_hp)}
    return result


def if_less_zero(hp: int) -> int:
    return 0 if hp <= 0 else hp
