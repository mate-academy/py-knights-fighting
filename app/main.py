from app.knight import Knight
from app.config import KNIGHTS


def battle(knights: dict) -> dict:
    knight1 = Knight(
        knights.get("lancelot").get("name"),
        knights.get("lancelot").get("power"),
        knights.get("lancelot").get("hp"),
        knights.get("lancelot").get("armour"),
        knights.get("lancelot").get("weapon"),
        knights.get("lancelot").get("potion")
    )
    knight2 = Knight(
        knights.get("arthur").get("name"),
        knights.get("arthur").get("power"),
        knights.get("arthur").get("hp"),
        knights.get("arthur").get("armour"),
        knights.get("arthur").get("weapon"),
        knights.get("arthur").get("potion")
    )
    knight3 = Knight(
        knights.get("mordred").get("name"),
        knights.get("mordred").get("power"),
        knights.get("mordred").get("hp"),
        knights.get("mordred").get("armour"),
        knights.get("mordred").get("weapon"),
        knights.get("mordred").get("potion")
    )
    knight4 = Knight(
        knights.get("red_knight").get("name"),
        knights.get("red_knight").get("power"),
        knights.get("red_knight").get("hp"),
        knights.get("red_knight").get("armour"),
        knights.get("red_knight").get("weapon"),
        knights.get("red_knight").get("potion")
    )

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
