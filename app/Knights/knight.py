from app.Staff.armour import Armour
from app.Staff.potion import Potion
from app.Staff.weapon import Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            health_points: int,
    ) -> None:
        self.name = name
        self.power = power
        self.health_points = health_points
        self.protection = 0

    def knight_stats_completing(
            self,
            armours: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.power += weapon.power + potion.power
        self.protection += sum([
            armour.protection for armour in armours
            if armours
        ]) + potion.protection
        self.health_points += potion.health
