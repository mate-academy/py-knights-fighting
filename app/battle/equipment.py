from app.knights.knights import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


def equip_knight(base_equip: dict) -> dict:
    fighter = Knight()

    for equip, value in base_equip.items():
        if equip == "name":
            fighter.name = value

        if equip == "power":
            fighter.base_power = value

        if equip == "hp":
            fighter.base_hp = value

        if equip == "armour" and value:
            for part in value:
                Armour(part["part"], part["protection"])
                fighter.protection += part["protection"]
                fighter.armour.append(Armour)

        if equip == "weapon":
            Weapon(value["name"], value["power"])
            fighter.base_power += value["power"]
            # Knight.weapon[Weapon.name] = Weapon.power

        if equip == "potion" and value:
            Potion(value["name"], value["effect"])
            # Knight.potion[Potion.name] = Potion.effect
            for stat, option in value["effect"].items():
                if stat == "power":
                    fighter.base_power += option
                if stat == "hp":
                    fighter.base_hp += option
                if stat == "protection":
                    fighter.protection += option

    return fighter.return_properties()
