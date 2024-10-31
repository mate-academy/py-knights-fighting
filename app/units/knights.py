from app.items.weapon import Weapon
from app.items.armour import Armour
from app.items.potion import Potion


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: list,
                 weapon: dict, potion=None, protection=0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(item["part"], item["protection"]) for item in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"], potion["effect"]) if potion else None
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
    def calculate_knight_power_hp_protection_with_staff(knights_list: list) -> list:
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
    def knights_battle(knights: list) -> list:
        # 1 Lancelot vs Mordred:
        for i in range(0, len(knights) + 1):
            if i < 2:
                knights[i].hp -= knights[i + 2].power - knights[i].protection
                knights[i + 2].hp -= knights[i].power - knights[i + 2].protection

                # check if someone fell in battle
                if knights[i].hp <= 0:
                    knights[i].hp = 0

                if knights[i + 2].hp <= 0:
                    knights[i + 2].hp = 0
            # i = 2
        return knights

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}
knights = Knight.create_knights(KNIGHTS)

for knight in knights:
    try:
        print(f" Name {knight.name}, Power {knight.power}, HP {knight.hp}, Protection {knight.protection}. \n")
        # print(f"Name: {knight.name}, HP: {knight.hp},"
        #     f" Power: {knight.power},"
        #       f" Armour part: {knight.armour[0].part},"
        #       f" Armour part: {knight.armour[0].protection}, \n"
        #       f" Armour 2 part: {knight.armour[1].part},"
        #       f" Armour 2 part: {knight.armour[1].protection}"
        #     f" Weapon name {knight.weapon.name},"
        #       f" Weapon power {knight.weapon.power}, \n"
        #       f" Potion hp {knight.potion.effect.hp}, "
        #       f"Potion power {knight.potion.effect.power},"
        #       f" Potion protection {knight.potion.effect.protection} \n")
    except (AttributeError, IndexError):
        print(f"Name: {knight.name}, HP: {knight.hp},"
              f" Power: {knight.power},"
              f"Name: {knight.name} has no attribute armour \n"
              f" Weapon name {knight.weapon.name},"
              f" Weapon power {knight.weapon.power}, \n"
              f" Name: {knight.name} has no attribute 'effect' \n")
        # print(f"Name: {knight.name} has no attribute 'effect' \n")
        # print(f"Name: {knight.name} has no attribute armour \n")
knights_with_staff = Knight.calculate_knight_power_hp_protection_with_staff(knights)

for knight in knights_with_staff:
    print(f" Name {knight.name}, Power {knight.power}, HP {knight.hp}, Protection {knight.protection}. \n")
knights_battle = Knight.knights_battle(knights_with_staff)
for knight in knights_battle:
    print(f" Name {knight.name}: HP {knight.hp}")