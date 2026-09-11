from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:

    def __init__(self, knight: dict) -> None:
        self.stats = {"power": knight["power"],
                      "hp": knight["hp"],
                      "protection": 0}
        self.name = knight["name"]

        if knight["armour"]:
            self.armour = [Armour(armour_piece["part"],
                                  armour_piece["protection"])
                           for armour_piece
                           in knight["armour"]]
        else:
            self.armour = []
        self.weapon = Weapon(knight["weapon"]["name"],
                             knight["weapon"]["power"])
        if knight["potion"] is not None:
            self.potion = Potion(knight["potion"]["name"],
                                 knight["potion"]["effect"])
        else:
            self.potion = None

    def apply_armour(self) -> None:
        if self.armour:
            self.stats["protection"] += sum([part.protection
                                             for part in self.armour])

    def use_weapon(self) -> None:
        self.stats["power"] += self.weapon.power

    def drink_potion(self) -> None :
        if self.potion is not None:
            if "hp" in self.potion.effect:
                self.stats["hp"] += self.potion.effect["hp"]
            if "power" in self.potion.effect:
                self.stats["power"] += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.stats["protection"] += self.potion.effect["protection"]

    def start_duel(self, knight: Knight) -> None:
        self.stats["hp"] -= knight.stats["power"] - self.stats["protection"]
        knight.stats["hp"] -= self.stats["power"] - knight.stats["protection"]
        if knight.stats["hp"] < 0:
            knight.stats["hp"] = 0
            print(f"{knight.name} has fallen")
        if self.stats["hp"] < 0:
            self.stats["hp"] = 0
            print(f"{self.name} has fallen")
