from app.model.armour import Armour
from app.model.battle import Battle
from app.model.knight import Knight
from app.model.potion import Potion
from app.model.weapon import Weapon


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    lancelot = Knight("Lancelot", 35, 100, [], Weapon("Metal Sword", 50), Potion())
    arthur = Knight("Arthur", 45, 75, [Armour("helmet", 15), Armour("breastplate", 20), Armour("boots", 10)],
                    Weapon("Two-handed Sword", 55), Potion())
    mordred = Knight("Mordred", 30, 90, [Armour("breastplate", 15), Armour("boots", 10)], Weapon("Poisoned Sword", 60),
                     Potion("Berserk", {"power": 15, "hp": -5, "protection": 10}))
    red_knight = Knight("Red Knight", 40, 70, [Armour("breastplate", 25)], Weapon("Sword", 45),
                       Potion("Blessing", {"power": 5, "hp": 10}))

    # lancelot
    lancelot.calculate_final_stats()
    arthur.calculate_final_stats()
    mordred.calculate_final_stats()
    red_knight.calculate_final_stats()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle(lancelot, mordred).fight()

    # 2 Arthur vs Red Knight:
    Battle(arthur, red_knight).fight()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
