from app.participants.lancelot import lancelot
from app.participants.arthur import arthur
from app.participants.mordred import mordred
from app.participants.red_knight import red_knight
from app.knight import Knight
from app.fight import fight


def battle(knights: dict = None) -> dict:
    keys = ["lancelot", "mordred", "arthur", "red_knight"]
    knights_objs = {}
    source = {
        "lancelot": lancelot,
        "mordred": mordred,
        "arthur": arthur,
        "red_knight": red_knight,
    }
    for key in keys:
        if knights is None:
            config = source[key][key]
            knights_objs[key] = Knight(config)
        else:
            config = knights[key]
            knights_objs[key] = Knight(config)

    first_fight = fight(knights_objs["lancelot"], knights_objs["mordred"])
    second_fight = fight(knights_objs["arthur"], knights_objs["red_knight"])

    return {**first_fight, **second_fight}


if __name__ == "__main__":
    print(battle())
