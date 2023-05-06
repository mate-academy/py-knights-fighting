from app.stats.armor import Armour
from app.stats.weapon import Weapon
from app.stats.potion import Potion


class Knights:
    knights = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list["Armour"] = None,
            weapon: "Weapon" = None,
            potion: "Potion" = None
    ) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        Knights.knights[name] = self

    @staticmethod
    def registration(knights: dict) -> "Knights":
        for knight, stat in knights.items():
            Knights(
                name=stat["name"],
                power=stat["power"],
                hp=stat["hp"],
                armour=Armour.armour_registration(stat["armour"]),
                weapon=Weapon.weapon_registration(stat["weapon"]),
                potion=Potion.potion_registration(stat["potion"])
            )

    def apply_armour(self) -> int:
        for armour in self.armour:
            self.protection += armour.protection
        return self.protection

    def apply_weapon(self) -> int:
        self.power += self.weapon.power
        return self.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection

    def battle_check(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    @staticmethod
    def battle_preparations(knights: list["Knights"]) -> None:
        for knight in knights:
            knight.protection = Knights.apply_armour(knight)
            knight.power = Knights.apply_weapon(knight)
            Knights.apply_potion(knight)
