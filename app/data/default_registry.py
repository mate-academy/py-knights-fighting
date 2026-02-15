from app.domain.items import Weapon, Armour, Potion
from app.domain.registry import ItemRegistry

registry = ItemRegistry(
    weapons = {
        "metal_sword": Weapon("Metal Sword", 50),
        "two_handed_sword": Weapon("Two-handed Sword", 55),
        "poisoned_sword": Weapon("Poisoned Sword", 60),
        "sword": Weapon("Sword", 45)
    },
    armours = {
        "helmet": Armour("Helmet", 15),
        "breastplate_15": Armour("Breastplate", 15),
        "breastplate_20": Armour("Breastplate", 20),
        "breastplate_25": Armour("Breastplate", 25),
        "boots": Armour("Boots", 10),
    },
    potions = {
        "berserk": Potion(
            "Berserk", {
                "power": 15,
                "hp": -5,
                "protection": 10
            }
        ),
        "blessing": Potion(
            "Blessing", {
                "power": 5,
                "hp": 10,
            }
        )
    }
)