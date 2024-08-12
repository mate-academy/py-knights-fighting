from app.classes import Knight


def battle(knights_config: dict) -> dict:
    knights = {}

    for i in knights_config:
        knights[i] = Knight(
            knights_config[i]["name"],
            knights_config[i]["power"],
            knights_config[i]["hp"],
            knights_config[i]["armour"],
            knights_config[i]["weapon"],
            knights_config[i]["potion"]
        )

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for first_fiter, second_fiter in battles:
        power_second = knights[second_fiter].final_power
        protection_first = knights[first_fiter].final_protection
        damage_to_first = max(
            0,
            power_second - protection_first
        )
        knights[first_fiter].final_hp -= damage_to_first

        power_first = knights[first_fiter].final_power
        protection_second = knights[second_fiter].final_protection
        damage_to_second = max(
            0,
            power_first - protection_second
        )
        knights[second_fiter].final_hp -= damage_to_second

    for knight in knights.values():
        knight.final_hp = max(0, knight.final_hp)

    return {knight.name: knight.final_hp for knight in knights.values()}
