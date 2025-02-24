from app.config import KNIGHTS
from app.knight import Knight
from app.battle import battle


def main() -> None:
    # Створюємо лицарів
    lancelot = Knight(**KNIGHTS["lancelot"])
    mordred = Knight(**KNIGHTS["mordred"])
    arthur = Knight(**KNIGHTS["arthur"])
    red_knight = Knight(**KNIGHTS["red_knight"])

    # Запускаємо битви
    battle_1_result = battle(lancelot, mordred)
    battle_2_result = battle(arthur, red_knight)

    # Виводимо результат
    print("Battle results:")
    print(battle_1_result)
    print(battle_2_result)


if __name__ == "__main__":
    main()