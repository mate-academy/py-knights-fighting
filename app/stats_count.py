"""
this module count hero stats for battle
"""


def heroes_stats_count(hero):
    name = hero.get("name")
    protection = sum([protect.get("protection") for protect in hero["armour"]])
    power = 0
    hp = 0

    for first_stats_key, first_stats_value in hero.items():
        if first_stats_key == "power" and first_stats_value is not None:
            power += first_stats_value
        if first_stats_key == "hp" and first_stats_value is not None:
            hp += first_stats_value
        if first_stats_key == "weapon" and first_stats_value is not None:
            power += hero["weapon"]["power"]
        if first_stats_key == "potion" and first_stats_value is not None:
            hp += hero["potion"]["effect"]["hp"]
            power += hero["potion"]["effect"]["power"]
            if hero["potion"]["effect"].get("protection") is not None:
                protection += hero["potion"]["effect"].get("protection")
    return [name, protection, power, hp]
