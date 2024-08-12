from app.classes import Knight


def damage_power(
        fiter_one: Knight,
        fiter_two: Knight
) -> None:
    damage = max(0, fiter_one.final_power - fiter_two.final_protection)
    fiter_two.final_hp -= damage


def battle(knights_config: dict) -> dict:

    knights = {
        knight_name: Knight(**knight_data)
        for knight_name, knight_data in knights_config.items()
    }

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for first_fighter, second_fighter in battles:
        damage_power(knights[second_fighter], knights[first_fighter])
        damage_power(knights[first_fighter], knights[second_fighter])

    return {
        knight.name:
            max(0, knight.final_hp) for knight in knights.values()
    }
