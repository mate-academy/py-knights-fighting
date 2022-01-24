from app.fightitems.armour import Armour
from app.fightitems.potion import Potion
from app.fightitems.weapon import Weapon


class Knight:
    BASE_PROTECTION = 0

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion = None,
    ):
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self._apply_base_stats(name, power, hp)
        self._apply_armour()
        if potion is not None:
            self._apply_potion()

        self._apply_weapon()

    def _apply_base_stats(self, name, power, hp):
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = self.BASE_PROTECTION

    def _apply_armour(self):
        self.protection += sum(
            armour_obj.protection
            for armour_obj in self.armour
        )

    def _apply_potion(self):
        self.power += self.potion.power
        self.hp += self.potion.hp
        self.protection += self.potion.protection

    def _apply_weapon(self):
        self.power += self.weapon.power

    @staticmethod
    def create_knight(knight_dict):
        weapon = Weapon.create_weapon(knight_dict['weapon'])
        armour_list = [
            Armour.create_armour(armour_dict=armour_dict)
            for armour_dict in knight_dict['armour']
        ]
        potion = None

        if (potion_dict := knight_dict['potion']) is not None:
            potion = Potion.create_potion(potion_dict=potion_dict)

        knight = Knight(
            name=knight_dict['name'],
            hp=knight_dict['hp'],
            power=knight_dict['power'],
            armour=armour_list,
            weapon=weapon,
            potion=potion,
        )
        return knight

    def battle(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
