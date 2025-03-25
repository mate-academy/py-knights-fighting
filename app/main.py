from config import KNIGHTS


def battle(knights):
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    for knight in knights.values():
        knight.apply_potion_effects()

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
