from app.knights.weapon import weapon_power_count
from app.knights.potion import potion_power_hp_protection
from app.knights.armour import armour_protection
from app.knights.knights import knights


def calculate_all_stats(knights_config: dict) -> dict:
    stats = {}
    for name, value in weapon_power_count(knights_config).items():
        power_final = 0
        hp_final = 0
        protection_final = 0
        power_final += (weapon_power_count(knights_config)[name] +
                        potion_power_hp_protection(knights_config)[name]["power"] +
                        knights(knights_config)[name]["power"])
        hp_final += (potion_power_hp_protection(knights_config)[name]["hp"] +
                     knights(knights_config)[name]["hp"])
        potion_long = potion_power_hp_protection(knights_config)[name]["protection"]
        protection_final += (potion_long +
                             armour_protection(knights_config)[name])
        stats[name] = {"power": power_final,
                       "hp": hp_final,
                       "protection": protection_final,
                       "knight_name": knights(knights_config)[name]["knight_name"]}
    weapon_power_count(knights_config)
    potion_power_hp_protection(knights_config)
    armour_protection(knights_config)
    knights(knights_config)
    return stats
