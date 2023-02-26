from __future__ import annotations
from typing import Any


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: Any,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_equipment(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]


lancelot = Knight("Lancelot",
                  35,
                  100,
                  [],
                  {
                      "name": "Metal Sword",
                      "power": 50,
                  },
                  None)

arthur = Knight("Artur",
                45,
                75,
                [
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
                {
                    "name": "Two-handed Sword",
                    "power": 55,
                },
                None)

mordred = Knight("Mordred",
                 30,
                 90,
                 [
                     {
                         "part": "breastplate",
                         "protection": 15,
                     },
                     {
                         "part": "boots",
                         "protection": 10,
                     }
                 ],
                 {
                     "name": "Poisoned Sword",
                     "power": 60,
                 },
                 {
                     "name": "Berserk",
                     "effect": {
                         "power": +15,
                         "hp": -5,
                         "protection": +10
                     }
                 })

red_knight = Knight("Red Knight",
                    40,
                    70,
                    [
                        {
                            "part": "breastplate",
                            "protection": 25,
                        }
                    ],
                    {
                        "name": "Sword",
                        "power": 45
                    },
                    {
                        "name": "Blessing",
                        "effect": {
                            "hp": +10,
                            "power": +5,
                        }
                    })

knights_list = [lancelot, arthur, mordred, red_knight]
