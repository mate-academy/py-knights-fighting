from app.knight.knight import Knight
from app.knight.knight import get_hp_of_knight, get_protection_of_knight, get_power_of_knight
from typing import List


def get_hp_after_battle(attacker: Knight, defender: Knight) -> int:
    # Отримуємо базові значення для атакуючого та захисника
    attacker_power = get_power_of_knight(attacker)
    defender_protection = get_protection_of_knight(defender)

    # Обчислюємо залишкові очки здоров'я для захисника після бою
    defender_hp = get_hp_of_knight(defender) - (attacker_power - defender_protection)

    # Повертаємо максимальне значення між 0 та залишковим здоров'ям
    return max(0, defender_hp)


knights_list = [
    Knight("Arthur", 70, armour=[{'part': 'helmet', 'protection': 15}, {'part': 'breastplate', 'protection': 20}, {'part': 'boots', 'protection': 25}],
           potion={"effect": {"hp": 10, "power": 5}, "name": "Blessing"}),
    Knight("Lancelot", 100, armour=[{'part': 'helmet', 'protection': 20}], potion=None),
    Knight("Mordred", 50, armour=[{'part': 'helmet', 'protection': 10}], potion=None),
    Knight("Red Knight", 80, armour=[{'part': 'helmet', 'protection': 10}, {'part': 'breastplate', 'protection': 20}, {'part': 'boots', 'protection': 25}],
           potion=None),
]


def battle(knights: List[Knight]):
    battle_pairs = [
        ("Arthur", "Red Knight"),
        ("Lancelot", "Mordred"),
    ]

    # Ініціалізація результатів перед боєм для кожного лицаря
    results = {knight.name: get_hp_of_knight(knight) for knight in knights}  # Звертаємося до атрибута 'name' кожного об'єкта 'Knight'

    # Проходимо через всі пари лицарів і проводимо бої
    for attacker_name, defender_name in battle_pairs:
        # Знаходимо об'єкти лицарів по іменах
        attacker = next(knight for knight in knights if knight.name == attacker_name)
        defender = next(knight for knight in knights if knight.name == defender_name)

        # Отримуємо залишкове HP для захисника після бою
        defender_hp_after_battle = get_hp_after_battle(attacker, defender)

        # Оновлюємо HP захисника
        results[defender.name] = defender_hp_after_battle

    return results
