from app.items.weapon import Weapon
from app.items.potion import Potion
from app.items.armour import Armour


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self._power = power
        self._hp = hp
        self._protection = 0
        self._weapon: Weapon
        self._potion: Potion | None = None
        self._armours: list = []

    @property
    def power(self) -> int:
        return self._power + self._weapon.power

    @property
    def hp(self) -> int:
        return self._hp

    def get_damage(self, damage: int) -> None:
        calc_damage = (damage - self.get_protection())
        self._hp -= calc_damage
        if self._hp < 0:
            self._hp = 0

    def attach_items(self, armours: list,
                     weapon: dict, potion: dict | None) -> None:
        for armour_item in armours:
            self._armours.append(Armour.create_armour(armour_item))
        self._weapon = Weapon(weapon["name"], weapon["power"])
        if potion is not None:
            self._potion = Potion.create_potion(config=potion)

    def prepare_to_battle(self) -> None:
        if isinstance(self._potion, Potion):
            self._protection += self._potion.protection
            self._hp += self._potion.hp
            self._power += self._potion.power

    @staticmethod
    def create_knight(config: dict) -> "Knight":
        knight = Knight(config["name"], config["power"], config["hp"])
        knight.attach_items(config["armour"],
                            config["weapon"], config["potion"])
        return knight

    def get_protection(self) -> int:
        protection = self._protection
        for armour in self._armours:
            protection += armour.protection
        return protection
