from app.equip.armour import Armour
from app.equip.potion import Potion
from app.equip.weapon import Weapon


class Hero:
    def __init__(self, stats: dict):
        self.stats = stats
        self.name = stats["name"]
        self.hp = stats["hp"]
        self.power = stats["power"]
        self.protection = 0
        self.cringe_bar = False

    def apply_quip(self) -> None:
        weapon = Weapon()
        self.power += weapon.get_weapon(self.stats["weapon"])

        armour = Armour(self.stats["armour"])
        self.protection += armour.get_armour()

        potion = Potion(self.stats["potion"])
        potion.get_potion(self)
