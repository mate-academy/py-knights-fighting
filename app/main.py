from app.characters.parser import parse
from app.characters.knights import Knight

from app.knights_info import KNIGHTS


def check_hp(battler: Knight) -> None:
    if battler.hp <= 0:
        battler.hp = 0


def fight(first_battler: Knight, second_battler: Knight) -> dict:
    first_battler.hp -= second_battler.power - first_battler.armour
    second_battler.hp -= first_battler.power - second_battler.armour
    check_hp(first_battler)
    check_hp(second_battler)
    return {
        first_battler.name: first_battler.hp,
        second_battler.name: second_battler.hp,
    }


def battle(knights_config: dict) -> dict:
    battlers = parse(knights_config)
    lancelot = battlers[0]
    arthur = battlers[1]
    mordred = battlers[2]
    red_knight = battlers[3]

    return fight(lancelot, mordred) | fight(arthur, red_knight)
