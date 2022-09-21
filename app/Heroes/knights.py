from app.config.equip import Armour, Weapon
from app.config.baffs import Buffs


class Ricar:
    def __init__(self, config: dict):
        self.config = config
        self.power = config["power"]
        self.name = config["name"]
        self.hp = config["hp"]
        self.protection = 0

    def take_ammunition(self) -> None:
        weapon = Weapon()
        self.power += weapon.get_weapon(self.config["weapon"])
        armour = Armour(self.config["armour"])
        self.protection += armour.get_armour()
        buffs = Buffs(self.config["potion"])
        buffs.take_buff(self)
