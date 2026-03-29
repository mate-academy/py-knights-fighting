from app.equipments.armour import Armour
from app.equipments.potion import Potion
from app.equipments.weapon import Weapon
from app.knights import Knights

knights_dict = {"lancelot": Knights(
    "Lancelot",
    power=35,
    hp=100,
    armours=[],
    weapon=Weapon("Metal Sword", 50),
    potion=None
),
    "mordred": Knights(
        "Mordred",
        power=30,
        hp=90,
        armours=[Armour("breastplate", 10), Armour("boots", 15)],
        weapon=Weapon("Poisoned Sword", 60),
        potion=Potion("Berserk", effect={"power": 15,
                                         "hp": -5,
                                         "protection": 10})
),
    "arthur": Knights(
        "Arthur",
        power=45,
        hp=75,
        armours=[Armour("helmet", 15),
                 Armour("breastplate", 20),
                 Armour("boots", 10)],
        weapon=Weapon("Two-handed Sword", 55),
        potion=None
),
    "red knight": Knights(
        "Red Knight",
        power=40,
        hp=70,
        armours=[Armour("breastplate", 25)],
        weapon=Weapon("Sword", 45),
        potion=Potion("Blessing", effect={"power": 5, "hp": 10})
)
}


def battle(knights_dict: dict) -> dict:
    result = {}
    result.update(
        knights_dict["lancelot"].battle_khights(knights_dict["mordred"])
    )
    result.update(
        knights_dict["arthur"].battle_khights(knights_dict["red knight"])
    )
    return result


print(battle(knights_dict))
