from typing import Dict
from knight import Armour, Weapon, Potion, Knight
from battle import Battle


def create_knights() -> Dict[str, Knight]:
    knights = {
        "lancelot": Knight(
            name="Lancelot",
            power=35,
            hp=100,
            armour=[],
            weapon=Weapon(name="Metal Sword", power=50),
            potion=Potion(name="None", effect={})  # No effect potion
        ),
        "arthur": Knight(
            name="Arthur",
            power=45,
            hp=75,
            armour=[
                Armour(part="helmet", protection=15),
                Armour(part="breastplate", protection=20),
                Armour(part="boots", protection=10)
            ],
            weapon=Weapon(name="Two-handed Sword", power=55),
            potion=Potion(name="None", effect={})  # No effect potion
        ),
        "mordred": Knight(
            name="Mordred",
            power=30,
            hp=90,
            armour=[
                Armour(part="breastplate", protection=15),
                Armour(part="boots", protection=10)
            ],
            weapon=Weapon(name="Poisoned Sword", power=60),
            potion=Potion(name="Berserk", effect={"power": 15, "hp": -5, "protection": 10})
        ),
        "red_knight": Knight(
            name="Red Knight",
            power=40,
            hp=70,
            armour=[Armour(part="breastplate", protection=25)],
            weapon=Weapon(name="Sword", power=45),
            potion=Potion(name="Blessing", effect={"hp": 10, "power": 5})
        )
    }
    return knights


def main() -> None:
    knights = create_knights()
    battle1 = Battle(knights["lancelot"], knights["mordred"])
    battle2 = Battle(knights["arthur"], knights["red_knight"])

    result1 = battle1.fight()
    result2 = battle2.fight()

    battle_results = {**result1, **result2}
    print(battle_results)


if __name__ == "__main__":
    main()
