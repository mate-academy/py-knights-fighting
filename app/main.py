from app.knights.knight import Knight
from app.knights.config import knights_data, battles


def battle(knights_config: dict) -> dict:
    # Initialize instances of Knight class
    knights = {key: Knight(**knight) for key, knight in knights_config.items()}

    # Prepare all knights for fights(apply potions, weapons, armor)
    for knight in knights.values():
        knight.prepare_for_battle()

    # Fight battles from config parameter
    for first_fighter, second_fighter in battles:
        knights[first_fighter].battle(
            knights[second_fighter])

    # Return battle results:
    return {
        knight.name: knight.hp for knight in knights.values()
    }


print(battle(knights_data))
