from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


def battle(knights_config: dict) -> dict:
    # Создаем объекты рыцарей
    knights = {
        key: Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=[Armour(**part) for part in config["armour"]],
            weapon=Weapon(**config["weapon"]),
            potion=Potion(**config["potion"]) if config["potion"] else None,
        )
        for key, config in knights_config.items()
    }

    # Пары для битвы
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    # Результаты битв
    results = {}

    for knight1_key, knight2_key in battles:
        knight1 = knights[knight1_key]
        knight2 = knights[knight2_key]

        # Рассчитываем характеристики рыцарей
        stats1 = knight1.calculate_stats()
        stats2 = knight2.calculate_stats()

        # Расчет урона
        stats1["hp"] -= max(0, stats2["power"] - stats1["protection"])
        stats2["hp"] -= max(0, stats1["power"] - stats2["protection"])

        # Убедимся, что HP не меньше 0
        stats1["hp"] = max(0, stats1["hp"])
        stats2["hp"] = max(0, stats2["hp"])

        # Сохраняем результаты
        results[knight1.name] = stats1["hp"]
        results[knight2.name] = stats2["hp"]

    return results
