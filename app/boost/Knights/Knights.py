from app.boost.Armour import Armour
from app.boost.Potion import Potion
from app.boost.Weapon import Weapon


class Knights:

    def __init__(self, knight_param: dict) -> None:

        self.name = knight_param["name"]
        self.power = knight_param["power"]
        self.hp = knight_param["hp"]
        self.armour = Armour(knight_param["armour"])
        self.weapon = Weapon(knight_param["weapon"])
        self.potion = Potion(knight_param["potion"]) \
            if knight_param["potion"] else None
        self.protection = 0

    def prepare_to_battle(self) -> None:
        Armour.apply_armour(self.armour, self)
        Weapon.apply_weapon(self.weapon, self)
        if self.potion:
            Potion.apply_potion(self.potion, self)
