from app.knight_equipment.armour import Armour
from app.knight_equipment.potion import Potion
from app.knight_equipment.weapon import Weapon


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: (dict, None)) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> dict:
        if self.potion:
            potion = Potion(self.potion["name"], self.potion["effect"])
        else:
            potion = Potion("No potion available")

        total_hp = self.hp + potion.drink_potion()["effect_hp"]

        weapon = Weapon(self.weapon["name"], self.weapon["power"])
        total_power = self.power + weapon.equip_weapon() +\
            potion.drink_potion()["effect_power"]

        armour_list = Armour(self.armour)
        total_protection = potion.drink_potion()["effect_protection"] + \
            armour_list.equip_armour()
        self.hp = total_hp
        self.power = total_power
        self.protection = total_protection
        # return {"hp": total_hp,
        #         "protection": total_protection,
        #         "power": total_power}

    def is_dead(self) -> bool:
        if self.hp < 0:
            print(f"{self.name} is dead!")
            return True
        return False


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
