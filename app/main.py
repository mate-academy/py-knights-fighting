from player.knights import Knights
from player.data import data_character


def battle(knights_сonfig: list) -> dict:
    knights_dict = {}
    for i in range(0, len(knights_сonfig) - 1, 2):
        knights_сonfig[i].hp -= max(knights_сonfig[i + 1].power
                                    - knights_сonfig[i].protection, 0)
        knights_сonfig[i + 1].hp -= max(knights_сonfig[i].power
                                        - knights_сonfig[i + 1].protection, 0)

        knights_dict[knights_сonfig[i].name] = knights_сonfig[i].hp
        knights_dict[knights_сonfig[i + 1].name] = knights_сonfig[i + 1].hp
    return knights_dict


knights_сonfig = Knights.character(data_character())
print(battle(knights_сonfig))
