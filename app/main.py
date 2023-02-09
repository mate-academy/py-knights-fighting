from app.buttle.action import make_knights
from app.buttle.knights_data import knights
from app.buttle.models import Knight
from app.buttle.start import start_fight


def battle(knights_config: dict) -> dict:
    knights_instances = make_knights(knights_config)

    start_fight([knights_instances[0], knights_instances[2]])
    start_fight([knights_instances[1], knights_instances[3]])

    return Knight.knights_to_dict(knights_instances)


print(battle(knights))
