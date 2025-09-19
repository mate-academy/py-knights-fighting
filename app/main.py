from app.utils.prepare import prepare_knight
from app.utils.fight import fight


def battle(knights_config: dict) -> dict:
    # Підготовка всіх лицарів у циклі
    prepared = {
        name: prepare_knight(data) for name, data in knights_config.items()
    }

    # Пара боїв
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    result = {}
    for k1, k2 in pairs:
        result.update(fight(prepared[k1], prepared[k2]))

    return result

