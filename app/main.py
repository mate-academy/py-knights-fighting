from app.knights.KnightsTemplate import KnightsTemplate


def battle() -> dict:
    lancelot = KnightsTemplate(
        name="Lancelot",
        power=35,
        hp=75,
        armour=[],
        weapon={
            "name": "Metal Sword",
            "power": 50,
        },
        potion={},
    )

    arthur = KnightsTemplate(
        name="Arthur",
        power=45,
        hp=75,
        armour=[
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
        weapon={
            "name": "Two-handed Sword",
            "power": 55,
        },
        potion={}
    )

    mordred = KnightsTemplate(
        name="Mordred",
        power=30,
        hp=90,
        armour=[
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        weapon={
            "name": "Poisoned Sword",
            "power": 60,
        },
        potion={
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    )

    red_knight = KnightsTemplate(
        name="Red Knight",
        power=40,
        hp=70,
        armour=[
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        weapon={
            "name": "Sword",
            "power": 45
        },
        potion={
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    )
    fighters_types = [lancelot, mordred, arthur, red_knight]
    knight: KnightsTemplate
    for knight in fighters_types:
        knight.add_power()
        knight.add_protection()
        knight.apply_potion()

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    if lancelot.hp <= 0:
        lancelot.hp = 0
    if mordred.hp <= 0:
        mordred.hp = 0
    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle())
