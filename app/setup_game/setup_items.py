from app.buffs.PotionEffects import PotionEffects
from app.items.potions import Potion
from app.items.armour import Armour
from app.items.weapons import Weapon


def get_weapon(name: str, power: int) -> Weapon:
    return Weapon(name, power)


def get_armour(part: str, protection: int) -> Armour:
    return Armour(part, protection)


def get_item_effects(effects: dict) -> PotionEffects:
    power = effects.get("power", 0)
    protection = effects.get("protection", 0)
    hp = effects.get("hp", 0)
    effect_instance = PotionEffects(
        hp, power, protection
    )
    return effect_instance


def get_potion(name: str, effect: dict) -> Potion:
    effect_instance = get_item_effects(effect)
    return Potion(name, effect_instance)
