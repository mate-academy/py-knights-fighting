from app.knight import Knight
from app.knights_stats import knights_stats


def create_knight(name: str, knights: dict, ) -> Knight:
    kwargs = knights.get(name)
    knight = Knight(**kwargs)
    return knight


def battle(knights_config: dict) -> dict:
    lancelot = create_knight("lancelot", knights_config)
    arthur = create_knight("arthur", knights_config)
    mordred = create_knight("mordred", knights_config)
    red_knight = create_knight("red_knight", knights_config)

    knights_list = [lancelot, arthur, mordred, red_knight]
    for each in range(len(knights_list)):
        knights_list[each].knights_config()

    results = {}

    lancelot.after_battle(mordred)
    arthur.after_battle(red_knight)
    for knight in knights_list:
        results.update({knight.name: knight.hp})
    return results


print(battle(knights_stats))
