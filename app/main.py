from app.characters.parser import parse
from app.characters.knights import Knight


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

    return (fight(battlers["Lancelot"], battlers["Mordred"])
            | fight(battlers["Arthur"], battlers["Red Knight"]))
