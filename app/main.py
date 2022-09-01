from app.Knights import Knights
from app.Knights import Battle
from app.Knights import battle_preparation as b_p


def battle(knights_config):
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    b_p.battle_preparation(lancelot, mordred, arthur, red_knight)
    Battle.battle_knight(lancelot, mordred)
    Battle.battle_knight(arthur, red_knight)

    return {lancelot["name"]: lancelot["hp"]}


print(battle(Knights))
