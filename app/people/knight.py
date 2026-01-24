from app.things.armour import Armour
from app.things.potion import Potion
from app.things.weapon import Weapon


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armours = []
        self.weapon = None
        self.potion = None

    def add_armour(self, armour: Armour) -> None:
        self.armours.append(armour)
        self.protection += armour.protection

    def add_armours_list(self, armours: list[dict]) -> None:
        for armour in armours:
            self.add_armour(
                Armour.create_armour_from_dict(armour)
            )

    def add_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += self.weapon.power

    def add_potion(self, potion: Potion | None) -> None:
        if potion is None:
            return
        self.potion = potion

        character_stat = ["hp", "power", "protection"]
        for stat in character_stat:
            setattr(self,
                    stat,
                    getattr(self, stat) + getattr(self.potion, stat))

    @classmethod
    def create_knight_from_dict(cls, dictionary: dict) -> "Knight":
        knight = cls(dictionary["name"],
                     dictionary["power"],
                     dictionary["hp"])

        knight.add_potion(
            Potion.create_potion_from_dict(dictionary=dictionary["potion"])
        )
        knight.add_weapon(
            Weapon.create_weapon_from_dict(dictionary=dictionary["weapon"])
        )
        knight.add_armours_list(armours=dictionary["armour"])

        return knight

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        self.after_fight()
        other.after_fight()

    def after_fight(self) -> None:
        if self.hp <= 0:
            self.hp = 0
