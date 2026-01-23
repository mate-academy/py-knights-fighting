from typing import Optional

from app.items.weapon import Weapon
from app.items.armour import Armour
from app.items.potion import Potion


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: list,
                 weapon: dict, potion: Optional[Potion] = None,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(item["part"],
                              item["protection"]) for item in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"],
                             potion["effect"]) if potion else None
        self.protection = protection

    @staticmethod
    def create_knights(knights_dict: dict) -> list:
        knights_list = []
        for knight_data in knights_dict.values():
            knight = Knight(
                name=knight_data["name"],
                power=knight_data["power"],
                hp=knight_data["hp"],
                armour=knight_data["armour"],
                weapon=knight_data["weapon"],
                potion=knight_data.get("potion")
            )
            knights_list.append(knight)
        return knights_list

    @staticmethod
    def calculate_knights_with_staff(knights_list: list) -> list:
        for knight in knights_list:
            for armour in knight.armour:
                knight.protection += armour.protection
            knight.power += knight.weapon.power
            if knight.potion is not None:
                if knight.potion.effect.power:
                    knight.power += knight.potion.effect.power
                if knight.potion.effect.protection:
                    knight.protection += knight.potion.effect.protection
                if knight.potion.effect.hp:
                    knight.hp += knight.potion.effect.hp
        return knights_list

    @staticmethod
    def knights_battle(knights: list) -> dict:
        # 1 Lancelot vs Mordred:
        total_knights_battle_dict = {}
        for i in range(0, len(knights) + 1):
            if i < 2:
                knights[i].hp -= knights[i + 2].power - knights[i].protection
                knights[i + 2].hp -= (knights[i].power
                                      - knights[i + 2].protection)
                if knights[i].hp <= 0:
                    knights[i].hp = 0

                if knights[i + 2].hp <= 0:
                    knights[i + 2].hp = 0
                total_knights_battle_dict[knights[i].name] = knights[i].hp
                total_knights_battle_dict[knights[i + 2].name]\
                    = knights[i + 2].hp
        return total_knights_battle_dict
