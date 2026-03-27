from app.warriors.knights import Knights


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, value in knights_config.items():
        knight = Knights(value["name"], value["power"], value["hp"])
        knight.apply_armour(value["armour"])
        knight.apply_weapon(value["weapon"])
        knight.apply_potion(value["potion"])
        knights[key] = knight

    knights["lancelot"].hp -= (knights["mordred"].power
                               - knights["lancelot"].protection)
    knights["mordred"].hp -= (knights["lancelot"].power
                              - knights["mordred"].protection)
    knights["arthur"].hp -= (knights["red_knight"].power
                             - knights["arthur"].protection)
    knights["red_knight"].hp -= (knights["arthur"].power
                                 - knights["red_knight"].protection)
    for knight in knights.values():
        if knight.hp < 0:
            knight.hp = 0
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["red_knight"].name: knights["red_knight"].hp
    }
