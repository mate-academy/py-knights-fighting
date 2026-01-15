from models import Knight
from battle import battle
from typing import Tuple


def create_knights() -> Tuple[Knight, Knight]:
    lancelot = Knight(
        name="Lancelot",
        power=35,
        hp=100,
        armour=[Armour("helmet", 15), Armour("breastplate", 30)],
        weapon=Weapon("Long Sword", 40),
        potion=Potion("Strength Potion", {"power": 10})
    )

    arthur = Knight(
        name="Arthur",
        power=40,
        hp=90,
        armour=[Armour("shield", 20)],
        weapon=Weapon("Excalibur", 50),
        potion=None
    )

    return lancelot, arthur


def main() -> None:
    lancelot, arthur = create_knights()
    result = battle(lancelot, arthur)
    print(result)


if __name__ == "__main__":
    main()
