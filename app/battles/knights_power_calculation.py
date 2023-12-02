from app.knights.knight import Knight
from app.battles.knights_creation import KnightsCreation
from app.main import KNIGHTS


class PowerCalculation:
    def __init__(self, knight: Knight) -> None:
        self.knight = knight

    def power_calculation(self) -> Knight:
        if hasattr(self.knight, "weapon"):
            self.knight.power += self.knight.weapon.power
        if hasattr(self.knight, "armour"):
            self.knight.protection = 0
            self.knight.protection += sum(unit.protection for unit in self.knight.armour)
        if hasattr(self.knight, "potion"):
            if "power" in self.knight.potion.effect:
                self.knight.power += self.knight.potion.effect["power"]

            if "protection" in self.knight.potion.effect:
                self.knight.protection += self.knight.potion.effect["protection"]

            if "hp" in self.knight.potion.effect:
                self.knight.hp += self.knight.potion.effect["hp"]
        return self.knight


create = KnightsCreation(KNIGHTS)
game_knight2 = KnightsCreation.knight_create(create, "red_knight")
knight_with_power = PowerCalculation(game_knight2)
game_knight = PowerCalculation.power_calculation(knight_with_power)
print(game_knight.name, game_knight.power, game_knight.hp, game_knight.weapon.power)
