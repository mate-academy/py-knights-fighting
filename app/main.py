from app.preparation.health import calculate_hp
from app.preparation.armour import apply_armour
from app.preparation.power import get_power
from app.fight.knights_fight import two_knights_fight
from app.data.knights_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    prepared_data = {}

    calculators = {
        "hp": calculate_hp,
        "power": get_power,
        "protection": apply_armour,
    }

    for knight in knights_config:
        prepared_data[knight] = {
            "name": knights_config[knight]["name"],
            **{
                stat: func(knights_config, knight)
                for stat, func in calculators.items()
            },
        }

    two_knights_fight(prepared_data["lancelot"], prepared_data["mordred"])
    two_knights_fight(prepared_data["arthur"], prepared_data["red_knight"])

    return {
        prepared_data[knight]["name"]: prepared_data[knight]["hp"]
        for knight in prepared_data
    }


print(battle(KNIGHTS))
