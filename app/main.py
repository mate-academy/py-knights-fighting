from app.knights_attributes import KNIGHTS
from app.prepare_k import prepare_knight
from app.fight import fight


def battle(knights_config: dict) -> dict:
    for knight_name, knight in knights_config.items():
        prepare_knight(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    lancelot["hp"], mordred["hp"] = fight(lancelot, mordred)
    arthur["hp"], red_knight["hp"] = fight(arthur, red_knight)

    return {
        knight["name"]:
            knight["hp"] for knight in
        [lancelot, arthur, mordred, red_knight]}


print(battle(KNIGHTS))
