from app.constants import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # Создаем объекты рыцарей
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    # 1) Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # 2) Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Возвращаем результаты
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
