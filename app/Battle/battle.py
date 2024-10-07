def battle(knights_attr: dict):
    knights_attr["lancelot"].hp -= knights_attr["mordred"].power - knights_attr["lancelot"].protection
    knights_attr["mordred"].hp -= knights_attr["lancelot"].power - knights_attr["mordred"].protection

    # check if someone fell in battle
    if knights_attr["lancelot"].hp <= 0:
        knights_attr["lancelot"].hp = 0

    if knights_attr["mordred"].hp <= 0:
        knights_attr["mordred"].hp = 0

    # 2 Arthur vs Red Knight:
    knights_attr["arthur"].hp -= knights_attr["red_knight"].power - knights_attr["arthur"].protection
    knights_attr["red_knight"].hp -= knights_attr["arthur"].power - knights_attr["red_knight"].protection

    # check if someone fell in battle
    if knights_attr["arthur"].hp <= 0:
        knights_attr["arthur"].hp = 0

    if knights_attr["red_knight"].hp <= 0:
        knights_attr["red_knight"].hp = 0

    return {
        knights_attr["lancelot"].name: knights_attr["lancelot"].hp,
        knights_attr["arthur"].name: knights_attr["arthur"].hp,
        knights_attr["mordred"].name: knights_attr["mordred"].hp,
        knights_attr["red_knight"].name: knights_attr["red_knight"].hp,
    }
#     knights_attr_values = list(knights_attr.values())
#     result = {}
#     for stats in range(0, len(knights_attr_values) // 2):
#         first_knight = knights_attr_values[stats]
#         second_knight = knights_attr_values[stats + 2]
#         first_knight.hp -= second_knight.power - first_knight.protection
#         second_knight.hp -= first_knight.power - second_knight.protection
#         if first_knight.hp <= 0:
#             first_knight.hp = 0
#         if second_knight.hp <= 0:
#             second_knight.hp = 0
#         result.update({first_knight.name: first_knight.hp, second_knight.name: second_knight.hp})
#     return result
