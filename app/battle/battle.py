from app.creating.knight import Knight
from app.creating.weapon import Weapon
from app.creating.armour import Armour
from app.creating.potion import Potion


class Battle:
    @staticmethod
    def start_battle(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        if knight_1.hp < 0:
            knight_1.hp = 0
        if knight_2.hp < 0:
            knight_2.hp = 0

    @staticmethod
    def prepare_battle(knightsconfig: dict) -> dict:
        knights = {}
        for value, item in knightsconfig.items():
            knight = knightsconfig[value]
            # Create knights
            knights[knight["name"]] = Knight(
                knight["name"],
                knight["power"],
                knight["hp"])
            # equip weapon
            knights[knight["name"]].equip_weapon(
                Weapon(knight["weapon"]["name"],
                       knight["weapon"]["power"]))

            for armour in knight["armour"]:
                knights[knight["name"]].equip_armor(
                    Armour(armour["part"], armour["protection"]))

            if knight["potion"] is not None:
                knights[knight["name"]].use_potion(
                    Potion(knight["potion"]["name"],
                           knight["potion"]["effect"]))
        return knights
