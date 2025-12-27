from app.knights_stats.create_knights import prepare_knight
from app.knights_stats.general import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot, mordred, arthur, red_knight = prepare_knight(knights_config)
    knights_pairs = [(lancelot, mordred), (arthur, red_knight)]
    for first_knight, second_knight in knights_pairs:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection
        first_knight.check_hp()
        second_knight.check_hp()

    knights = [lancelot, mordred, arthur, red_knight]
    return {knight.name: knight.hp for knight in knights}


if __name__ == "__main__":
    print(battle(KNIGHTS))
