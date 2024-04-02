from __future__ import annotations
from app.armed.weapon import Weapon
from app.armed.armour import Armour
from app.armed.potion import Potion


class Warrior:
    # Basic qualities of warrior, human like
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self. hp = hp


class Knight:
    #  The warrior is prepared to be Knight
    def __init__(self,
                 warrior: Warrior,
                 power: int = 0,
                 hp: int = 0,
                 protection: int = 0,
                 weapon: Weapon = None,
                 armours: list[Armour] = None,
                 potion: Potion = None
                 ) -> None:
        self.warrior = warrior
        self.power = self.warrior.power
        self.hp = self.warrior.hp
        self.protection = protection
        self.weapon = weapon
        self.armours = armours
        self.potion = potion

    def weapon_on(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += self.weapon.power

    def armour_on(self, armours: list[Armour]) -> None:
        self.armours = armours
        for armour in armours:
            self.protection += armour.protection

    def potion_on(self, potion: Potion) -> None:
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]

    # Battle option implemented like quality of the Knight
    def __mul__(self, other: Knight) -> None:
        # if isinstance(other, Knight):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check knight HP
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
        # warrior new HP must be the same as knight's
        self.warrior.hp = self.hp
        other.warrior.hp = other.hp


if __name__ == "__main__":
    warriors = {
        "lancelot": Warrior(name="Lancelot", power=35, hp=100),
        "arthur": Warrior(name="Arthur", power=45, hp=75),
        "mordred": Warrior(name="Mordred", power=30, hp=90),
        "red_knight": Warrior(name="Red_knight", power=40, hp=70)
    }

    print(" ----------- warriors --------------------")
    for man, soldier in warriors.items():
        print(f"{man} = {soldier.__dict__}")

    weapons = {
        "lancelot": Weapon(name="Metal Sword", power=50),
        "arthur": Weapon(name="Two-handed Sword", power=55),
        "mordred": Weapon(name="Poisoned Sword", power=60),
        "red_knight": Weapon(name="Sword", power=45)
    }

    armour_s = {
        "helmet_15": Armour("helmet", 15),
        "breastplate_20": Armour("breastplate", 20),
        "boots_10": Armour("boots", 10),
        "breastplate_15": Armour("breastplate", 15),
        "breastplate_25": Armour("breastplate", 25)
    }

    berserk = Potion(name="Berserk",
                     effect={
                         "power": +15,
                         "hp": -5,
                         "protection": +10
                     })
    blessing = Potion(name="Blessing",
                      effect={
                          "hp": +10,
                          "power": +5
                      })

    knight_arms = {
        "lancelot": [],
        "arthur": [
            armour_s["helmet_15"],
            armour_s["breastplate_20"],
            armour_s["boots_10"]
        ],
        "mordred": [
            armour_s["breastplate_15"],
            armour_s["boots_10"]
        ],
        "red_knight": [
            armour_s["breastplate_25"]
        ]
    }

    knights_potion = {
        "mordred": berserk,
        "red_knight": blessing,
    }

    knight = dict()
    print("\n ----------- KNIGHTS --------------------")
    for soldier in warriors:
        knight[soldier] = Knight(warriors[soldier])
        knight[soldier].weapon_on(weapons[soldier])
        knight[soldier].armour_on(knight_arms[soldier])
        if soldier in knights_potion:
            knight[soldier].potion_on(knights_potion[soldier])

        print(f"{knight[soldier].warrior.name} = "
              f"power: {knight[soldier].power}, "
              f"hp: {knight[soldier].hp}, "
              f"protection: {knight[soldier].protection}"
              )

    print("\n ----------- BATTLE --------------------")
    # 1 Lancelot vs Mordred:
    knight["lancelot"] * knight["mordred"]
    # 2 Arthur vs Red Knight:
    knight["arthur"] * knight["red_knight"]

    for soldier in warriors:
        print(f"{knight[soldier].warrior.name} = "
              f"power: {knight[soldier].power}, "
              f"hp: {knight[soldier].hp}, "
              f"protection: {knight[soldier].protection}"
              )
