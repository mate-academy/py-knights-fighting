from app.Inventory.potion import Potion
from app.Inventory.armour import Armour
from app.Inventory.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_weapon(self, knight: dict) -> None:
        weapon = Weapon(knight["weapon"]["name"], knight["weapon"]["power"])
        self.power += weapon.power

    def get_armour(self, knight: dict) -> None:
        if knight["armour"]:
            for arm in knight["armour"]:
                armour = Armour(arm["part"], arm["protection"])
                self.protection += armour.protection

    def get_potion(self, knight: dict) -> None:
        if knight["potion"]:
            potion = Potion(
                knight["potion"]["name"],
                knight["potion"]["effect"]
            )
            if "hp" in potion.effect:
                self.hp += potion.effect["hp"]
            if "power" in potion.effect:
                self.power += potion.effect["power"]
            if "protection" in potion.effect:
                self.protection += potion.effect["protection"]
