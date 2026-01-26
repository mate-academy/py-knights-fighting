from app.knight import Knight
from app.config import KNIGHTS


def run_duel(attacker: Knight, defender: Knight) -> None:
    # Формула: damage = power ворога - protection захисника
    damage = attacker.power - defender.protection
    # Якщо захист більший за удар, шкода = 0
    if damage < 0:
        damage = 0
    defender.take_damage(damage)


def battle(knights_config: dict = KNIGHTS) -> dict:
    # 1. Створюємо об'єкти лицарів
    lancelot = Knight.from_config(knights_config["lancelot"])
    arthur = Knight.from_config(knights_config["arthur"])
    mordred = Knight.from_config(knights_config["mordred"])
    red_knight = Knight.from_config(knights_config["red_knight"])

    # 2. Підготовуємо їх (рахуємо броню, зілля тощо)
    lancelot.prepare_stats()
    arthur.prepare_stats()
    mordred.prepare_stats()
    red_knight.prepare_stats()

    # 3. Проводимо бої згідно з завданням
    # Lancelot vs Mordred
    run_duel(attacker=lancelot, defender=mordred)
    run_duel(attacker=mordred, defender=lancelot)

    # Arthur vs Red Knight
    run_duel(attacker=arthur, defender=red_knight)
    run_duel(attacker=red_knight, defender=arthur)

    # 4. Повертаємо результати
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
