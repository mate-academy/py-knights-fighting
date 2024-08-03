from app.hero import Hero


def battle(config: dict) -> dict:

    lancelot = Hero.create_from_config(config.get("lancelot"))
    arthur = Hero.create_from_config(config.get("arthur"))
    mordred = Hero.create_from_config(config.get("mordred"))
    red_knight = Hero.create_from_config(config.get("red_knight"))

    for knight in (lancelot, arthur, mordred, red_knight):
        knight.prepare_to_battle()

    lancelot.attack(mordred)
    mordred.attack(lancelot)

    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
