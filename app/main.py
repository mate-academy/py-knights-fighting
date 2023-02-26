from __future__ import annotations

from app.class_knights import knights_list, Knight


def battle(knights: list) -> dict:
    # battle preparations
    for knight in knights:
        knight.apply_equipment()

    def check_death(member: Knight) -> None:
        if member.hp <= 0:
            member.hp = 0

    def local_battle(first_member: Knight, second_member: Knight) -> None:
        first_member.hp -= \
            second_member.power - first_member.protection
        second_member.hp -= \
            first_member.power - second_member.protection

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]
    # BATTLE:

    # 1 Lancelot vs Mordred:
    local_battle(lancelot, mordred)

    # check if someone fell in battle
    check_death(lancelot)
    check_death(mordred)

    # 2 Arthur vs Red Knight:
    local_battle(arthur, red_knight)

    # check if someone fell in battle
    check_death(arthur)
    check_death(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


battle(knights_list)
