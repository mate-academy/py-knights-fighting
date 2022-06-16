from app.equipment import equip_armour, equip_weapon, use_potion
from app.knights import KNIGHTS
from app.fight_logic import fight


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    lancelot = knightsConfig["lancelot"]
    equip_armour(lancelot)
    equip_weapon(lancelot)
    use_potion(lancelot)

    arthur = knightsConfig["arthur"]
    equip_armour(arthur)
    equip_weapon(arthur)
    use_potion(arthur)

    mordred = knightsConfig["mordred"]
    equip_armour(mordred)
    equip_weapon(mordred)
    use_potion(mordred)

    red_knight = knightsConfig["red_knight"]
    equip_armour(red_knight)
    equip_weapon(red_knight)
    use_potion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    fight1 = fight(lancelot, mordred)
    fight2 = fight(arthur, red_knight)
    fight1.update(fight2)
    return fight1


print(battle(KNIGHTS))
