from battle knight import Knight
from battle weapon import Weapon
from battle potion import Potion

def main():
    # Initialize knights, weapons, and potions
    weapon1 = Weapon("Sword", 10)
    potion1 = Potion("Strength", power_effect=5)
    knight1 = Knight("Arthur", 50, 100, weapon=weapon1, potion=potion1)

    weapon2 = Weapon("Axe", 15)
    potion2 = Potion("Healing", hp_effect=20)
    knight2 = Knight("Lancelot", 45, 120, weapon=weapon2, potion=potion2)

    # Battle
    knight1.battle(knight2)
    print(f"{knight1.name} HP: {knight1.hp}, {knight2.name} HP: {knight2.hp}")

if __name__ == "__main__":
    main()
