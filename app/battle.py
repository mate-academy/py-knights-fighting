from app.preparations import prepare, Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection


def check_injuries_of(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def battle_of(the_contestants: dict) -> dict:
    knights = prepare(the_contestants)

    fight(knights.get("lancelot"), knights.get("mordred"))
    check_injuries_of(knights.get("lancelot"))
    check_injuries_of(knights.get("mordred"))

    fight(knights.get("arthur"), knights.get("red_knight"))
    check_injuries_of(knights.get("arthur"))
    check_injuries_of(knights.get("red_knight"))

    return {
        "Lancelot": knights.get("lancelot").hp,
        "Arthur": knights.get("arthur").hp,
        "Mordred": knights.get("mordred").hp,
        "Red Knight": knights.get("red_knight").hp,
    }
