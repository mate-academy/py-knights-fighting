from app.championship.attributes import attributes
from app.championship.combat import combat


def battle(knights: dict) -> dict:
    for knight_name in knights:
        attributes(knights[knight_name])
    combat(knights["lancelot"], knights["mordred"])
    combat(knights["arthur"], knights["red_knight"])
    return {knight["name"]: knight["hp"] for knight in knights.values()}
