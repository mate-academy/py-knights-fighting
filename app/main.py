from __future__ import annotations
from app.knights import Knights

lancelot = Knights(
    "Lancelot",
    35,
    100,
    [],
    {
        "name": "Metal Sword",
        "power": 50
    },
    None)

arthur = Knights(
    "Arthur",
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
        }],
    {
        "name": "Two-handed Sword",
        "power": 55,
    },
    None)

mordred = Knights(
    "Mordred",
    30,
    90,
    [
        {
            "part": "breastplate",
            "protection": 15
        },
        {
            "part": "boots",
            "protection": 10
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
            "protection": +10,
        }
    })

red_knight = Knights(
    "Red Knight",
    40,
    70,
    [
        {
            "part": "breastplate",
            "protection": 25
        },
    ],
    {
        "name": "Sword",
        "power": 45,
    },
    {
        "name": "Blessing",
        "effect": {
            "hp": +10,
            "power": +5,
        }
    })


def action(inst1: Knights, inst2: Knights,
           inst3: Knights, inst4: Knights) -> dict:
    inst1.battle(inst2)
    inst3.battle(inst4)
    return {
        inst1.name: inst1.hp,
        inst2.name: inst2.hp,
        inst3.name: inst3.hp,
        inst4.name: inst4.hp
    }

# print(action(lancelot, mordred, arthur, red_knight))

# # POWER CHECK
# print(lancelot.weapon)
# print(lancelot.add_power())
# print(lancelot.potion_benefits()[0])
# print(lancelot.power)
#
# # print(arthur.weapon)
# # print(arthur.add_power())
# # print(arthur.potion_benefits()[0])
# print(arthur.power)
#
# # print(mordred.weapon)
# # print(mordred.add_power())
# # print(mordred.potion_benefits()[0])
# print(mordred.power)
#
# # print(red_knight.weapon)
# # print(red_knight.add_power())
# # print(red_knight.potion_benefits()[0])
# print(red_knight.power)
#
# # PROTECTION
# print(lancelot.protection)
# print(arthur.protection)
# print(mordred.protection)
# print(red_knight.protection)
#
# print(f"{lancelot.hp} -= {arthur.power} - {lancelot.protection}")
# print(f"{arthur.hp} -= {lancelot.power} - {arthur.protection}")
#
# lancelot.hp -= arthur.power - lancelot.protection
# arthur.hp -= lancelot.power - arthur.protection
#
# print(lancelot.hp)
# print(arthur.hp)
#
# print(f"{mordred.hp} -= {red_knight.power} - {mordred.protection}")
# print(f"{red_knight.hp} -= {mordred.power} - {red_knight.protection}")
#
# mordred.hp -= red_knight.power - mordred.protection
# red_knight.hp -= mordred.power - red_knight.protection
#
# print(mordred.hp)
# print(red_knight.hp)

# print(action(lancelot, mordred, arthur, red_knight))

# # POWER CHECK
# print(lancelot.weapon)
# print(lancelot.add_power())
# print(lancelot.potion_benefits()[0])
# print(lancelot.power)
#
# # print(arthur.weapon)
# # print(arthur.add_power())
# # print(arthur.potion_benefits()[0])
# print(arthur.power)
#
# # print(mordred.weapon)
# # print(mordred.add_power())
# # print(mordred.potion_benefits()[0])
# print(mordred.power)
#
# # print(red_knight.weapon)
# # print(red_knight.add_power())
# # print(red_knight.potion_benefits()[0])
# print(red_knight.power)
#
# # PROTECTION
# print(lancelot.protection)
# print(arthur.protection)
# print(mordred.protection)
# print(red_knight.protection)
#
# print(f"{lancelot.hp} -= {arthur.power} - {lancelot.protection}")
# print(f"{arthur.hp} -= {lancelot.power} - {arthur.protection}")
#
# lancelot.hp -= arthur.power - lancelot.protection
# arthur.hp -= lancelot.power - arthur.protection
#
# print(lancelot.hp)
# print(arthur.hp)
#
# print(f"{mordred.hp} -= {red_knight.power} - {mordred.protection}")
# print(f"{red_knight.hp} -= {mordred.power} - {red_knight.protection}")
#
# mordred.hp -= red_knight.power - mordred.protection
# red_knight.hp -= mordred.power - red_knight.protection
#
# print(mordred.hp)
# print(red_knight.hp)
