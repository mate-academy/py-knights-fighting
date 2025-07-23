from app.knights import Knight
from app.items import Armour, Weapon, Potion

metal_sword = Weapon(name="Metal Sword", effect={"power": 50})
sword = Weapon(name="Sword", effect={"power": 45})
two_handed_sword = Weapon(name="Two-handed Sword", effect={"power": 55})
poisoned_sword = Weapon(name="Poisoned Sword", effect={"power": 60})

red_knight_breastplate = Armour(part="breastplate", effect={"protection": 25})
mordred_breastplate = Armour(part="breastplate", effect={"protection": 15})
mordred_boots = Armour(part="boots", effect={"protection": 10})
arthur_breastplate = Armour(part="breastplate", effect={"protection": 20})
helmet = Armour(part="helmet", effect={"protection": 15})
arthur_boots = Armour(part="boots", effect={"protection": 10})

blessing_potion = Potion(name="Blessing", effect={"hp": 10, "power": 15})
berserk = Potion(
    name="Berserk",
    effect={"power": +15, "hp": -5, "protection": +10}
)


lancelot = Knight(
    name="Lancelot",
    power=35,
    hp=100,
    armour=None,
    weapon=[metal_sword],
    potion=None
)
arthur = Knight(
    name="Arthur",
    power=45,
    hp=75,
    armour=[helmet, arthur_breastplate, arthur_boots],
    weapon=[two_handed_sword],
    potion=None
)
mordred = Knight(
    name="Mordred",
    power=70,
    hp=90,
    armour=[mordred_breastplate, mordred_boots],
    weapon=[poisoned_sword],
    potion=[berserk]
)
red_knight = Knight(
    name="Red Knight",
    power=10,
    hp=70,
    armour=[red_knight_breastplate],
    weapon=[sword],
    potion=[blessing_potion]
)

knights = [lancelot, mordred, arthur, red_knight]


def battle_preparations(knight: Knight) -> None:
    if knight.armour is not None:
        for item in knight.armour:
            knight.apply_effect(item)
    if knight.weapon is not None:
        for item in knight.weapon:
            knight.apply_effect(item)
    if knight.potion is not None:
        for item in knight.potion:
            knight.apply_effect(item)


def battle_fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp = knight2.power - knight1.protection
    knight2.hp = knight1.power - knight2.protection
    if knight1.hp < 0:
        knight1.hp = 0
    if knight2.hp < 0:
        knight2.hp = 0


def battle(knights_list: list[Knight]) -> dict:
    for knight in knights_list:
        battle_preparations(knight)
    battle_fight(knights[0], knights[1])
    battle_fight(knights[2], knights[3])
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }

print(battle(knights))
