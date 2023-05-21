from app.preparations.participant import Participant
from app.organizations.arena import prepare_knight, fight
from app.organizations.initialization import initialization as start
from app.organizations.data import dict_of_knights as knights


def battle(knight_config: dict) -> dict:
    start(knight_config)
    for knight_name in Participant.people.keys():
        prepare_knight(knight_name)
    fight("Lancelot", "Mordred")
    fight("Arthur", "Red Knight")
    result = Participant.give_result()
    return result


print(battle(knights))
