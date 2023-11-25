from app.knights import Knight
from app.battle import battle as knightbattle


def battle(knights_config: dict) -> dict:

    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    knightbattle(lancelot, mordred)
    knightbattle(arthur, red_knight)

    print(f"{lancelot.name}: {lancelot.hp} HP")
    print(f"{arthur.name}: {arthur.hp} HP")
    print(f"{mordred.name}: {mordred.hp} HP")
    print(f"{red_knight.name}: {red_knight.hp} HP")
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
