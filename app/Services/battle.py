from app.Objects.knight import Knight


def battle(knights: dict[str, Knight]) -> dict[str, int]:
    # Перевірка, чи всі об'єкти є екземплярами класу Knight
    for key, knight in knights.items():
        if not isinstance(knight, Knight):
            raise TypeError(f"Object {key} is not an instance of Knight")

    # 1. Дістаємо лицарів
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    # 2. Бої
    fight(lancelot, mordred)
    fight(arthur, red_knight)

    # 3. Результат
    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }


def fight(knight1: Knight, knight2: Knight) -> None:
    # удар knight1 по knight2
    knight2.get_damage(knight1)

    # удар knight2 по knight1
    knight1.get_damage(knight2)