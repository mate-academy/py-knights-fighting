from app.class_knight import Knight


def one_battle(first_knight: str,
               second_knight: str,
               third_knight: str,
               fourth_knight: str) -> dict:
    result = {}
    Knight.list_knight[first_knight].config_hp -= \
        (Knight.list_knight[second_knight].config_power
         - Knight.list_knight[first_knight].config_armour)
    Knight.list_knight[second_knight].config_hp -= (
        Knight.list_knight[first_knight].config_power
        - Knight.list_knight[second_knight].config_armour)
    Knight.list_knight[third_knight].config_hp -= (
        Knight.list_knight[fourth_knight].config_power
        - Knight.list_knight[third_knight].config_armour)
    Knight.list_knight[fourth_knight].config_hp -= (
        Knight.list_knight[third_knight].config_power
        - Knight.list_knight[fourth_knight].config_armour)
    if Knight.list_knight[first_knight].config_hp <= 0:
        Knight.list_knight[first_knight].config_hp = 0
    if Knight.list_knight[second_knight].config_hp <= 0:
        Knight.list_knight[second_knight].config_hp = 0
    if Knight.list_knight[third_knight].config_hp <= 0:
        Knight.list_knight[third_knight].config_hp = 0
    if Knight.list_knight[fourth_knight].config_hp <= 0:
        Knight.list_knight[fourth_knight].config_hp = 0
    result[Knight.list_knight[first_knight].name] = (
        Knight.list_knight[first_knight].config_hp)
    result[Knight.list_knight[third_knight].name] = (
        Knight.list_knight[third_knight].config_hp)
    result[Knight.list_knight[second_knight].name] = (
        Knight.list_knight[second_knight].config_hp)
    result[Knight.list_knight[fourth_knight].name] = (
        Knight.list_knight[fourth_knight].config_hp)
    return result
