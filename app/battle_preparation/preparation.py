from app.battle_preparation.knight import Knight
import app.battle_preparation.creating_obj as cr


def battle_preparation(dictionary: dict) -> list[Knight]:
    knights = cr.creating_knights(dictionary=dictionary)
    armours = cr.creating_armors(dictionary=dictionary)
    weapons = cr.creating_weapons(dictionary=dictionary)
    potions = cr.creating_potions(dictionary=dictionary)

    for knight in knights:
        knight.protection = sum(
            [armour.protection for armour in armours[knight.name]])
        knight.power += weapons[knight.name].power
        if knight.name in potions:
            for effect in potions[knight.name].effect:
                if effect == "power":
                    knight.power += potions[knight.name].effect["power"]
                elif effect == "hp":
                    knight.hp += potions[knight.name].effect["hp"]
                elif effect == "protection":
                    knight.protection += \
                        potions[knight.name].effect["protection"]
    return knights
