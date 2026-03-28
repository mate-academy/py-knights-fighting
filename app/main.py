from app.knights.knights_config import KNIGHTS
from app.knights.knight import Knight
from app.knights.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight.from_config(config)
        for name, config in knights_config.items()
    }

    res_1 = Battle(knights["lancelot"], knights["mordred"]).battle()
    res_2 = Battle(knights["arthur"], knights["red_knight"]).battle()

    # 3. Об'єднуємо результати
    return res_1 | res_2


print(battle(KNIGHTS))
