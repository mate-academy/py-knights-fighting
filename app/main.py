from app.battle import battle
from app.knights import Knights
from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


def main() -> None:
    # Creating knights
    knights = [
        Knights(
            name="Lancelot",
            power=35,
            hp=100,
            armour=[],
            weapon=Weapon("Metal Sword", 50)
        ),
        Knights(
            name="Mordred",
            power=30,
            hp=90,
            armour=[
                Armour("breastplate", 15),
                Armour("boots", 10),
            ],
            weapon=Weapon("Poisoned Sword", 60),
            potion=Potion("Berserk",
                          {"power": +15, "hp": -5, "protection": +10})
        ),
        Knights(
            name="Arthur",
            power=45,
            hp=75,
            armour=[
                Armour("helmet", 15),
                Armour("breastplate", 20),
                Armour("boots", 10)
            ],
            weapon=Weapon("Two-handed Sword", 55)
        ),
        Knights(
            name="Red Knight",
            power=40,
            hp=70,
            armour=[
                Armour("breastplate", 25)
            ],
            weapon=Weapon("Sword", 45),
            potion=Potion("Blessing", {"hp": +10, "power": +5})
        )
    ]

    # Battle
    result = battle(knights)

    # Results
    print("Battle result:", result)


if __name__ == "__main__":
    main()
