from .Characters.knights import Knight


arthur = Knight(
    name="Arthur",
    hp=75,
    power=45,
    weapon={"name": "Two-handed Sword", "power": 55},
    armour=[
        {"part": "Helmet", "protection": 15},
        {"part": "Breastplate", "protection": 20},
        {"part": "Boots", "protection": 10}
    ],
    potion=None
)

lancelot = Knight(
    name="Lancelot",
    hp=35,
    power=100,
    weapon={"name": "Metal_sword", "power": 50},
    armour=[],
    potion=None,
)

mordred = Knight(
    name="Mordred",
    hp=30,
    power=90,
    weapon={"name": "poison_sword", "power": 60},
    armour=[
        {"part": "breastplate", "protection": 25},
        {"part": "boots", "protection": 10},
    ],
    potion={
        "name": "Berserk",
        "effect": {"hp": -5, "power": +15, "protection": +20},
    }
)

red_knight = Knight(
    name="Red Knight",
    hp=40,
    power=70,
    weapon={"name": "sword", "power": 45},
    armour=[
        {"part": "breastplate", "protection": 25}
    ],
    potion={
        "name": "Blessing",
        "effect": {"hp": +10, "power": +5, "protection": 0},
    }
)


def single_hit(knight1: Knight, knight2: Knight) -> None:

    dmg1 = max(0, knight1.power - knight2.protection)
    dmg2 = max(0, knight2.power - knight1.protection)

    knight2.hp -= dmg1
    knight1.hp -= dmg2

    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)


def battle(config: dict) -> dict:

    lancelot = Knight(**config["lancelot"])
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])

    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.prepare_to_battle()

    single_hit(lancelot, mordred)
    single_hit(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
