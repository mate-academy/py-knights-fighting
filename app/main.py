from app.preparing_knights.create import create_knights


def battle(knights: dict) -> dict:
    fighters = {
        name: create_knights(knight) for name, knight in knights.items()
    }

    lancelot = fighters.get("lancelot")
    mordred = fighters.get("mordred")
    arthur = fighters.get("arthur")
    red_knight = fighters.get("red_knight")

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    return {
        lancelot.name: max(0, lancelot.hp),
        arthur.name: max(0, arthur.hp),
        mordred.name: max(0, mordred.hp),
        red_knight.name: max(0, red_knight.hp),
    }
