from app.knights.cls_knight import Knight
from app.knights.Knights import KNIGHTS


def knights_fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights: dict) -> dict:
    lancelot = knights["lancelot"]
    knight_lancelot = Knight(
        lancelot["name"],
        lancelot["power"],
        lancelot["hp"],
        lancelot["armour"],
        lancelot["weapon"],
        lancelot["potion"]
    )
    knight_lancelot.prepare_for_battle()

    arthur = knights["arthur"]
    knight_arthur = Knight(
        arthur["name"],
        arthur["power"],
        arthur["hp"],
        arthur["armour"],
        arthur["weapon"],
        arthur["potion"]
    )
    knight_arthur.prepare_for_battle()

    mordred = knights["mordred"]
    knight_mordred = Knight(
        mordred["name"],
        mordred["power"],
        mordred["hp"],
        mordred["armour"],
        mordred["weapon"],
        mordred["potion"]
    )
    knight_mordred.prepare_for_battle()

    red_knight = knights["red_knight"]
    knight_red_knight = Knight(
        red_knight["name"],
        red_knight["power"],
        red_knight["hp"],
        red_knight["armour"],
        red_knight["weapon"],
        red_knight["potion"]
    )
    knight_red_knight.prepare_for_battle()

    knights_fight(knight_lancelot, knight_mordred)
    knights_fight(knight_arthur, knight_red_knight)

    return {
        knight_lancelot.name: knight_lancelot.hp,
        knight_arthur.name: knight_arthur.hp,
        knight_mordred.name: knight_mordred.hp,
        knight_red_knight.name: knight_red_knight.hp,
    }


print(battle(KNIGHTS))
