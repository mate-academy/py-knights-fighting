from app import config
from app.knight import Knight
from app.battle import fight


def battle(knights_config: dict) -> dict:
    for i in knights_config:
        knight_data = knights_config[i]
        knight = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armour=knight_data["armour"],
            weapon=knight_data["weapon"],
            potion=knight_data["potion"]
        )
        knights_config[i] = knight
        knights_config[i].prepare()

    result1 = fight(knights_config["lancelot"], knights_config["mordred"])
    result2 = fight(knights_config["arthur"], knights_config["red_knight"])
    return {**result1, **result2}


print(battle(config.KNIGHTS))
