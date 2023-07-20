from app.knight import Knight
from app.config import KNIGHTS


def battle(knights: dict) -> dict:
    knight1 = Knight(*[value for value in knights.get("lancelot").values()])
    knight2 = Knight(*[value for value in knights.get("arthur").values()])
    knight3 = Knight(*[value for value in knights.get("mordred").values()])
    knight4 = Knight(*[value for value in knights.get("red_knight").values()])

    def fight(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection
        if first_knight.hp <= 0:
            first_knight.hp = 0
        if second_knight.hp <= 0:
            second_knight.hp = 0

    knight1.preparation()
    knight2.preparation()
    knight3.preparation()
    knight4.preparation()
    fight(knight1, knight3)
    fight(knight2, knight4)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
        knight3.name: knight3.hp,
        knight4.name: knight4.hp
    }


print(battle(KNIGHTS))
