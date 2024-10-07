from app.models import Knight, Weapon, Armour, Potion
from app.battle import battle


KNIGHTS = {
    "lancelot": Knight(
        name="Lancelot",
        base_power=35,
        hp=100,
        armour=[],
        weapon=Weapon(name="Metal Sword", power=50),
        potion=None,
    ),
    "arthur": Knight(
        name="Arthur",
        base_power=45,
        hp=75,
        armour=[
            Armour(part="helmet", protection=15),
            Armour(part="breastplate", protection=20),
            Armour(part="boots", protection=10),
        ],
        weapon=Weapon(name="Two-handed Sword", power=55),
        potion=None,
    ),
    "mordred": Knight(
        name="Mordred",
        base_power=30,
        hp=90,
        armour=[
            Armour(part="breastplate", protection=15),
            Armour(part="boots", protection=10),
        ],
        weapon=Weapon(name="Poisoned Sword", power=60),
        potion=Potion(
            name="Berserk",
            effect={
                "power": 15,
                "hp": -5,
                "protection": 10,
            }
        ),
    ),
    "red_knight": Knight(
        name="Red Knight",
        base_power=40,
        hp=70,
        armour=[Armour(part="breastplate", protection=25)],
        weapon=Weapon(name="Sword", power=45),
        potion=Potion(
            name="Blessing",
            effect={
                "hp": 10,
                "power": 5,
            }
        ),
    ),
}


if __name__ == "__main__":
    results = battle(KNIGHTS)
    for name, hp in results.items():
        print(f"{name}: {hp} HP")
