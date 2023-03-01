from app.hero.knight import Knight
from app.file.descride_heros import describe_heros


def battle(describe_heros):
    lancelot = Knight.create_knight(describe_heros["lancelot"])
    arthur = Knight.create_knight(describe_heros["arthur"])
    mordred = Knight.create_knight(describe_heros["mordred"])
    red_knight = Knight.create_knight(describe_heros["red_knight"])

    lancelot.fight(mordred)

    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":

    print(battle(describe_heros))
