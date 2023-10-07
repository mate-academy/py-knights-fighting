from app.knight_stats import Knight
from app.battle_func import battle_action


def battle(knights_config: dict) -> dict:
    knights = knights_config

    knights_in_class = [Knight(knights.get(knight)) for knight in knights]

    for knight in knights_in_class:
        knight.apply_all()

    lancelot = knights_in_class[0]
    arthur = knights_in_class[1]
    mordred = knights_in_class[2]
    red_knight = knights_in_class[3]

    battle_action(lancelot, mordred)
    battle_action(arthur, red_knight)

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
