from app.knights.config import KNIGHTS
from app.knights.knight import Knight
from app.battle.fight import fight


def battle():
    # Створюємо об'єкти лицарів
    lancelot = Knight(**KNIGHTS["lancelot"])
    mordred = Knight(**KNIGHTS["mordred"])
    arthur = Knight(**KNIGHTS["arthur"])
    red_knight = Knight(**KNIGHTS["red_knight"])

    # Бої
    result1 = fight(lancelot, mordred)
    result2 = fight(arthur, red_knight)

    return result1, result2
