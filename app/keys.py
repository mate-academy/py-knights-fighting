from enum import Enum


class KeysKnight(Enum):
    NAME = "name"
    POWER = "power"
    HP = "hp"
    ARMOUR = "armour"
    WEAPON = "weapon"
    POTION = "potion"
    PROTECTION = "protection"


class KeysArmour(Enum):
    PART = "part"
    PROTECTION = "protection"


class KeysWeapon(Enum):
    NAME = "name"
    POWER = "power"


class KeysPotion(Enum):
    NAME = "name"
    EFFECT = "effect"
