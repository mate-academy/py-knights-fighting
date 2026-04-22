from app.knight.knights_config import KNIGHTS
from app.armour.part_armour import apply_armour
from app.weapon.weapon import apply_weapon
from app.potion.potion import apply_potion
from app.battle.battle import fight


def battle(knights_config: dict) -> dict:
    apply_armour(knights_config)
    apply_weapon(knights_config)
    apply_potion(knights_config)
    return fight(knights_config)


print(battle(KNIGHTS))
