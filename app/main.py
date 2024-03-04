from app.knights import Knight


def battle(knights_config: dict) -> dict:
    knights = {}

    for name, config in knights_config.items():
        knight = Knight(name=config["name"],
                        power=config["power"],
                        hp=config["hp"],
                        armour=config["armour"],
                        weapon=config["weapon"],
                        potion=config["potion"])
        knight.prepare_for_battle()
        knights[name] = knight

    knights["lancelot"].hp -= max(0, knights["mordred"].power
                                  - knights["lancelot"].protection)
    knights["mordred"].hp -= max(0, knights["lancelot"].power
                                 - knights["mordred"].protection)

    knights["arthur"].hp -= max(0, knights["red_knight"].power
                                - knights["arthur"].protection)
    knights["red_knight"].hp -= max(0, knights["arthur"].power
                                    - knights["red_knight"].protection)

    for knight in knights.values():
        if knight.hp < 0:
            knight.hp = 0

    return {knight.name: knight.hp for knight in knights.values()}
