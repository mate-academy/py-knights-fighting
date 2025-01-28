from app.models.knight import Knight
from app.config import KNIGHTS


def fight(knight1: Knight, knight2: Knight) -> dict:
    print(f"Початок бою: {knight1.name} ({knight1.hp} HP) vs {knight2.name} ({knight2.hp} HP)")
    while knight1.hp > 0 and knight2.hp > 0:
        damage_to_knight2 = max(knight1.power - knight2.protection, 0)
        knight2.hp -= damage_to_knight2
        print(f"{knight1.name} атакує {knight2.name}: завдано {damage_to_knight2}, залишилось {knight2.hp} HP")

        # Лицар 2 атакує лицаря 1
        damage_to_knight1 = max(knight2.power - knight1.protection, 0)
        knight1.hp -= damage_to_knight1
        print(f"{knight2.name} атакує {knight1.name}: завдано {damage_to_knight1}, залишилось {knight1.hp} HP")

        # Повернення результатів
    result = {
        knight1.name: max(knight1.hp, 0),
        knight2.name: max(knight2.hp, 0),
    }
    print(f"Результат бою: {result}")
    return result




