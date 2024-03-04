from app.knights.models.knight import Knight
from app.knights.models.armour import Armour
from app.knights.models.weapon import Weapon
from app.knights.models.potion import Potion


def create_knights() -> tuple:
    # Створення обладунку
    helmet = Armour("helmet", 15)
    breastplate = Armour("breastplate", 20)
    boots = Armour("boots", 10)
    mordred_breastplate = Armour("breastplate", 15)
    mordred_boots = Armour("boots", 10)
    red_knight_breastplate = Armour("breastplate", 25)

    # Створення зброї
    metal_sword = Weapon("Metal Sword", 50)
    two_handed_sword = Weapon("Two-handed Sword", 55)
    poisoned_sword = Weapon("Poisoned Sword", 60)
    sword = Weapon("Sword", 45)

    # Створення зілля
    berserk_potion = Potion("Berserk",
                            {"power": 15, "hp": -5, "protection": 10})
    blessing_potion = Potion("Blessing", {"hp": 10, "power": 5})

    # Створення лицарів
    lancelot = Knight("Lancelot", 35, 100, [],
                      metal_sword, None)
    arthur = Knight("Arthur", 45, 75,
                    [helmet, breastplate, boots],
                    two_handed_sword, None)
    mordred = Knight("Mordred", 30, 90,
                     [mordred_breastplate, mordred_boots],
                     poisoned_sword, berserk_potion)
    red_knight = Knight("Red Knight", 40, 70,
                        [red_knight_breastplate], sword, blessing_potion)

    return lancelot, arthur, mordred, red_knight


def battle(knight1: Knight, knight2: Knight) -> dict:
    knight1.apply_potion()
    knight1.apply_weapon()
    knight2.apply_potion()
    knight2.apply_weapon()

    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight2.hp -= max(0, knight1.power - knight2.protection)

    return {
        knight1.name: max(0, knight1.hp),
        knight2.name: max(0, knight2.hp),
    }


def main() -> None:
    lancelot, arthur, mordred, red_knight = create_knights()

    # Проведення битв і виведення результатів
    result1 = battle(lancelot, mordred)
    result2 = battle(arthur, red_knight)

    print("Battle 1 result:", result1)
    print("Battle 2 result:", result2)


if __name__ == "__main__":
    main()
