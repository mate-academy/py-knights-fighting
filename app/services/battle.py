from app.models.knight import Knight

def battle(knights_config):
    knights = {name: Knight(**data) for name, data in knights_config.items()}

    # Battle between Lancelot and Mordred
    knights["lancelot"].take_damage(knights["mordred"].power)
    knights["mordred"].take_damage(knights["lancelot"].power)

    # Battle between Arthur and Red Knight
    knights["arthur"].take_damage(knights["red_knight"].power)
    knights["red_knight"].take_damage(knights["arthur"].power)

    # Return the battle result
    return {knight.name: knight.hp for knight in knights.values()}
