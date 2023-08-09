from app.knights import Knight
from app.ammunition.weapon import Weapon
from app.ammunition.armour import Armour
from app.ammunition.potion import Potion


def dict_to_classes(dictionary: dict) -> list["Knight"]:
    knights = []
    for knight, stats in dictionary.items():
        armour = []
        for element in stats["armour"]:
            armour.append(Armour.from_element(element))
        knight = Knight(
            name=stats["name"],
            power=stats["power"],
            hp=stats["hp"],
            armour=armour,
            weapon=Weapon(
                name=stats["weapon"]["name"],
                power=stats["weapon"]["power"]
            ),
            potion=None if stats.get("potion") is None else Potion(
                name=stats["potion"]["name"],
                effect=stats["potion"]["effect"]
            )
        )
        knights.append(knight)
    return knights


def get_knights() -> list:
    lancelot = Knight(
        name="Lancelot",
        power=35,
        hp=100,
        armour=[],
        weapon=Weapon(name="Metal Sword", power=50),
        potion=None
    )
    arthur = Knight(
        name="Arthur",
        power=45,
        hp=75,
        armour=[
            Armour(part="helmet", protection=15),
            Armour(part="breastplate", protection=20),
            Armour(part="boots", protection=10)
        ],
        weapon=Weapon(name="Two-handed Sword", power=55),
        potion=None
    )
    mordred = Knight(
        name="Mordred",
        power=30,
        hp=90,
        armour=[
            Armour(part="breastplate", protection=15),
            Armour(part="boots", protection=10)
        ],
        weapon=Weapon(name="Poisoned Sword", power=60),
        potion=Potion(name="Berserk",
                      effect={
                          "power": +15,
                          "hp": -5,
                          "protection": +10,
                      })
    )
    red_knight = Knight(
        name="Red Knight",
        power=40,
        hp=70,
        armour=[Armour(part="breastplate", protection=25)],
        weapon=Weapon(name="Sword", power=45),
        potion=Potion(name="Blessing",
                      effect={
                          "hp": +10,
                          "power": +5,
                      })
    )
    return [lancelot, arthur, mordred, red_knight]
