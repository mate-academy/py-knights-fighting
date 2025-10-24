from app.knights.weapon import weapon_power_count
from app.knights.potion import potion_power_hp_protection
from app.knights.armour import armour_protection
from app.knights.knights import knights


def stat(dict_test: dict) -> dict:
    stats = {}
    for name, value in weapon_power_count(dict_test).items():
        power_final = 0
        hp_final = 0
        protection_final = 0
        power_final += (weapon_power_count(dict_test)[name] +
                        potion_power_hp_protection(dict_test)[name]["power"] +
                        knights(dict_test)[name]["power"])
        hp_final += (potion_power_hp_protection(dict_test)[name]["hp"] +
                     knights(dict_test)[name]["hp"])
        potion_long = potion_power_hp_protection(dict_test)[name]["protection"]
        protection_final += (potion_long +
                             armour_protection(dict_test)[name])
        stats[name] = {"power": power_final,
                       "hp": hp_final,
                       "protection": protection_final,
                       "knight_name": knights(dict_test)[name]["knight_name"]}
    weapon_power_count(dict_test)
    potion_power_hp_protection(dict_test)
    armour_protection(dict_test)
    knights(dict_test)
    return stats
