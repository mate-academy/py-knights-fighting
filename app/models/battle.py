from typing import Dict
from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    # Зберігаємо силу до бою
    power1 = knight1.power
    power2 = knight2.power

    knight1.take_damage(power2)
    knight2.take_damage(power1)


def battle(knights_config: dict) -> Dict[str, int]:
    # Створюємо екземпляри лицарів
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Проводимо бої
    fight(lancelot, mordred)
    fight(arthur, red_knight)

    # Повертаємо результат
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
