from player.knights import Knights
from player.data import data_character


def battle(knights_config: list) -> dict:
    knights_dict = {}
    for i in range(0, len(knights_config), 2):
        knights_config[i].hp -= max(knights_config[i + 1].power
                                    - knights_config[i].protection, 0)
        knights_config[i + 1].hp -= max(knights_config[i].power
                                        - knights_config[i + 1].protection, 0)

        knights_dict[knights_config[i].name] = knights_config[i].hp
        knights_dict[knights_config[i + 1].name] = knights_config[i + 1].hp
    return knights_dict


knights_config = Knights.character(data_character())
print(battle(knights_config))
