from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    @classmethod
    def create_knight(cls, config: dict) -> Knight:
        knight = cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
        )
        armour_list = []
        for item in config["armour"]:
            armour_list.append(
                Armour(part=item["part"], protection=item["protection"])
            )
        knight.apply_armour(armour_list)
        weapon = Weapon(
            name=config["weapon"]["name"],
            power=config["weapon"]["power"],
        )
        knight.apply_weapon(weapon)
        if config["potion"] is not None:
            potion = Potion(
                name=config["potion"]["name"],
                effect=config["potion"]["effect"],
            )
            knight.apply_potion(potion)
        return knight

    def apply_armour(self, armour: list[Armour]) -> None:
        for item in armour:
            self.protection += item.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def fight(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection
        self.check_hp()
        opponent.check_hp()
