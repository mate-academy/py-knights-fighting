from app.attributes.armor import Armour
from app.attributes.weapon import Weapon
from app.attributes.potion import Potion


class Knight:
    def __init__(self, param: dict) -> None:
        self.name = param['name']
        self.power = param['power']
        self.hp = param['hp']
        self.armour = Armour(param['armour'])
        self.weapon = Weapon(param['weapon'])
        self.potion = Potion(param['potion']) if param['potion'] else None
        self.protection = 0

    def preparation(self) -> None:
        Armour.use_armor(self.armour, self)
        Weapon.use_weapon(self.weapon, self)
        if self.potion:
            Potion.use_potion(self.potion, self)

    def check_hp(self) -> None:
        self.hp = self.hp if self.hp > 0 else 0
