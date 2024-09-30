from app.knights import Knight


def battle(knights_config: dict) -> dict:
    """
    Simulates a battle between knights based on their configuration.

    The function creates instances of the Knight class from the provided
    configuration, calculates their stats, and simulates pairwise battles
    between knights.

    Args:
        knights_config (dict): A dictionary containing the configuration of
                               knights, where each knight's name is mapped to
                               their stats.

    Returns:
        dict: A dictionary containing the final health points (hp) of all
              knights after the battle.
    """
    knights = {key: Knight(**value) for key, value in knights_config.items()}

    for knight in knights.values():
        knight.calculate_stats()

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for knight1, knight2 in battles:
        knights[knight1].take_damage(
            knights[knight2].total_power - knights[knight1].protection
        )
        knights[knight2].take_damage(
            knights[knight1].total_power - knights[knight2].protection
        )

    return {knight.name: knight.hp for knight in knights.values()}
