from app.knights.knights import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


def equip_knight(base_equip: dict) -> dict:
    fighter = Knight()

    for equip in base_equip:
        if equip == "name":
            fighter.name = base_equip.get(equip)

        if equip == "power":
            fighter.base_power = base_equip.get(equip)

        if equip == "hp":
            fighter.base_hp = base_equip.get(equip)

        if equip == "armour" and base_equip.get(equip):
            for part in base_equip.get(equip):
                Armour(part["part"], part["protection"])
                fighter.protection += part["protection"]
                fighter.armour.append(Armour)

        if equip == "weapon":
            Weapon(base_equip.get(equip)["name"],
                   base_equip.get(equip)["power"])
            fighter.base_power += base_equip.get(equip)["power"]

        if equip == "potion" and base_equip.get(equip):
            Potion(base_equip.get(equip)["name"],
                   base_equip.get(equip)["effect"])

            for stat, option in base_equip.get(equip)["effect"].items():
                if stat == "power":
                    fighter.base_power += option
                if stat == "hp":
                    fighter.base_hp += option
                if stat == "protection":
                    fighter.protection += option

    return fighter.return_properties()
