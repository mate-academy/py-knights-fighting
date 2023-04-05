from app.battle_knights.fighting import Battle
from app.creation_knights.knights_stats import Knight
from app.knight_dict import Knights


def battle(knights_config: dict) -> dict:
    # creation of a dictionary generator of class knights
    knights_list = {
        name: Knight(
            characteristics["name"],
            characteristics["power"],
            characteristics["hp"],
            characteristics["armour"],
            characteristics["weapon"],
            characteristics["potion"])
        for name, characteristics in knights_config.items()
    }

    # application of characteristics
    for characteristics in knights_list.values():
        Knight.apply_weapon(characteristics)
        Knight.apply_armour(characteristics)
        Knight.apply_potion(characteristics)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle.combat(knights_list["lancelot"], knights_list["mordred"])

    # 2 Arthur vs Red Knight:
    Battle.combat(knights_list["arthur"], knights_list["red_knight"])

    # check if someone fell in battle
    Battle.check_death(knights_list)

    # Return battle results:
    return {
        knights_list["lancelot"].name: knights_list["lancelot"].hp,
        knights_list["arthur"].name: knights_list["arthur"].hp,
        knights_list["mordred"].name: knights_list["mordred"].hp,
        knights_list["red_knight"].name: knights_list["red_knight"].hp,
    }


print(battle(Knights))
