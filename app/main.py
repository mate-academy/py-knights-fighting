from app.knight import Knight
from app.config import KNIGHTS


def battle(knights: dict) -> dict:
    knight1 = Knight(*knights.get("lancelot").values())
    knight2 = Knight(*knights.get("arthur").values())
    knight3 = Knight(*knights.get("mordred").values())
    knight4 = Knight(*knights.get("red_knight").values())

    knight1.prepare()
    knight2.prepare()
    knight3.prepare()
    knight4.prepare()
    Knight.fight(knight1, knight3)
    Knight.fight(knight2, knight4)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
        knight3.name: knight3.hp,
        knight4.name: knight4.hp
    }


print(battle(KNIGHTS))
