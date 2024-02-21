from app.mods.armour import Armour, get_armours
from app.mods.weapon import Weapon, get_weapon
from app.mods.potion import Potion, get_potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.potion = None
        self.armours = None
        self.weapon = None

    def add_armour(self, armours: list[Armour]) -> None:
        self.armours = armours
        for armor in armours:
            self.protection += armor.protection

    def add_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def add_potion(self, potion: Potion) -> None:
        self.potion = potion
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]


def create_knight(params: dict, name: str) -> Knight:
    params = params[name]
    knight_obj = Knight(
        params["name"],
        params["power"],
        params["hp"]
    )
    knight_obj.add_armour(get_armours(params["armour"]))
    knight_obj.add_weapon(get_weapon(params["weapon"]))
    if params["potion"] is not None:
        knight_obj.add_potion(get_potion(params["potion"]))

    return knight_obj


def fight(first_knight: Knight, second_knight: Knight) -> dict:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    if first_knight.hp < 0:
        first_knight.hp = 0
    if second_knight.hp < 0:
        second_knight.hp = 0

    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp
    }
