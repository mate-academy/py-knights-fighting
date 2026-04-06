from app.knights import Knights
from app.all_knights import KNIGHTS


def battle_preparations(knight: Knights) -> None:
    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()


def check_who_fell(knight: Knights) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def fight(knight1: Knights, knight2: Knights) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection


def battle(knight: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights = {element: Knights(knight=knight.get(element))
               for element in knight}
    for element in knights.values():
        battle_preparations(element)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(knights.get("lancelot"), knights.get("mordred"))
    check_who_fell(knights.get("lancelot"))
    check_who_fell(knights.get("mordred"))

    # 2 Arthur vs Red Knight:
    fight(knights.get("arthur"), knights.get("red_knight"))
    check_who_fell(knights.get("arthur"))
    check_who_fell(knights.get("red_knight"))

    # Return battle results:
    return {element.name: element.hp for element in knights.values()}


print(battle(KNIGHTS))
