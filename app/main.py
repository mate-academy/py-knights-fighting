from app.knight import Knight
from app.config import KNIGHTS


def run_duel(attacker: Knight, defender: Knight) -> None:
    damage = attacker.power - defender.protection
    if damage < 0:
        damage = 0
    defender.take_damage(damage)


def battle(knights_config: dict = KNIGHTS) -> dict:
    # Словник для зберігання готових об'єктів лицарів
    knights = {}

    # 1. & 2. Створюємо та готуємо лицарів у циклі
    for name, config in knights_config.items():
        knight = Knight.from_config(config)
        knight.prepare_stats()
        knights[name] = knight

    # Отримуємо потрібних лицарів зі словника для проведення боїв
    # (Ми знаємо ключі з конфігурації)
    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    # 3. Проводимо бої
    run_duel(attacker=lancelot, defender=mordred)
    run_duel(attacker=mordred, defender=lancelot)

    run_duel(attacker=arthur, defender=red_knight)
    run_duel(attacker=red_knight, defender=arthur)

    # 4. Формуємо результат через dict comprehension (виправлено Checklist #2)
    return {knight.name: knight.hp for knight in knights.values()}
