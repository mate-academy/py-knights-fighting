from typing import Dict
from models.knight import Knight
from models.armour import Armour
from models.weapon import Weapon
from models.potion import Potion
from models.magic import Magic


def get_knights_config() -> Dict[str, Knight]:
    return {
        "lancelot": Knight(
            name="Lancelot",
            base_power=35,
            base_hp=100,
            armour=[],  # No armour
            weapon=Weapon(name="Metal Sword", power=50),
            potion=None,
            magic=Magic(name="Seal of the Sun", base_power=10)
        ),
        "arthur": Knight(
            name="Arthur",
            base_power=45,
            base_hp=75,
            armour=[
                Armour(part="helmet", protection=15),
                Armour(part="breastplate", protection=20),
                Armour(part="boots", protection=10)
            ],
            weapon=Weapon(name="Two-handed Sword", power=55),
            potion=None,
            magic=None
        ),
        "mordred": Knight(
            name="Mordred",
            base_power=30,
            base_hp=90,
            armour=[
                Armour(part="breastplate", protection=15),
                Armour(part="boots", protection=10)
            ],
            weapon=Weapon(name="Poisoned Sword", power=60),
            potion=Potion(
                name="Berserk",
                base_effect={
                    "power": 15,         # ±5
                    "hp": -5,            # ±5
                    "protection": 10     # ±5
                },
            ),
            magic=None
        ),
        "red_knight": Knight(
            name="Red Knight",
            base_power=40,
            base_hp=70,
            armour=[
                Armour(part="breastplate", protection=25)
            ],
            weapon=Weapon(name="Sword", power=45),
            potion=Potion(
                name="Blessing",
                base_effect={
                    "hp": 10,         # ±5
                    "power": 5        # ±5
                },
            ),
            magic=None
        )
    }
