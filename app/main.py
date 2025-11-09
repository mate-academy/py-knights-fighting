from app.helpers.potion_usage import UsePotion
from app.helpers.knights_config import KNIGHTS
from app.helpers.apply_armour import Armour
from app.helpers.apply_weapon import Weapon
from app.knights.knights import Character


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Character("lancelot", 35, 100)
    lancelot.equip_character(knightsConfig)

    # apply armour
    lancelot_use_armour = Armour(lancelot)
    lancelot_use_armour.use_armour()

    # apply weapon
    lancelot_weapon = Weapon(lancelot)
    lancelot_weapon.use_weapon()

    # apply potion if exist
    lancelot_use_potion = UsePotion(lancelot)
    lancelot_use_potion.use_all_potion()

    # arthur
    arthur = Character("arthur", 45, 75)
    arthur.equip_character(knightsConfig)

    # apply armour
    arthur_use_armour = Armour(arthur)
    arthur_use_armour.use_armour()

    # apply weapon
    arthur_weapon = Weapon(arthur)
    arthur_weapon.use_weapon()

    # apply potion if exist
    arthur_use_potion = UsePotion(arthur)
    arthur_use_potion.use_all_potion()

    # mordred
    mordred = Character("mordred", 30, 90)
    mordred.equip_character(knightsConfig)

    # apply armour
    mordred_use_armour = Armour(mordred)
    mordred_use_armour.use_armour()

    # apply weapon
    mordred_weapon = Weapon(mordred)
    mordred_weapon.use_weapon()

    # apply potion if exist
    mordred_use_potion = UsePotion(mordred)
    mordred_use_potion.use_all_potion()

    # red_knight
    red_knight = Character("red_knight", 40, 70)
    red_knight.equip_character(knightsConfig)

    # apply armour
    red_knight_use_armour = Armour(red_knight)
    red_knight_use_armour.use_armour()

    # apply weapon
    red_knight_weapon = Weapon(red_knight)
    red_knight_weapon.use_weapon()

    # apply potion if exist
    red_knight_use_potion = UsePotion(red_knight)
    red_knight_use_potion.use_all_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        "Lancelot": lancelot.hp,
        "Arthur": arthur.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp,
    }


print(battle(KNIGHTS))
