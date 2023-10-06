from items.weapon import Weapon
from items.armour import Armour
from items.potion import Potion


class InitItems:

    @staticmethod
    def init_weapon(name: str, config: dict) -> Weapon:
        weapon_name = config.get(name).get("weapon").get("name")
        power = config.get(name).get("weapon").get("power")
        return Weapon(weapon_name, power)

    @staticmethod
    def init_armour(name: str, config: dict) -> list[Armour]:
        equipment = []
        for part_arm in config.get(name).get("armour"):
            part = part_arm.get("part")
            protect = part_arm.get("protection")
            equipment.append(Armour(part, protect))
        return equipment

    @staticmethod
    def init_potion(name: str, config: dict) -> Potion:
        if config.get(str(name)).get("potion"):
            potion_name = config.get(str(name)).get("potion").get("name")
            effect = config.get(str(name)).get("potion").get("effect")
            return Potion(potion_name, effect)
