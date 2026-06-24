from app.knight import Knight
from app.knights_data import KNIGHTS


def fight(knight_1: Knight, knight_2: Knight) -> None:
    power_1, power_2 = knight_1.power, knight_2.power
    knight_1.receive_damage(power_2)
    knight_2.receive_damage(power_1)


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight.from_dict(data) for key, data in knights_config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
