from app.knight import Knight
from app.knights_config import knights


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    # check if someone fell in fight
    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: dict[str, dict]) -> dict[str, int]:

    lancelot = Knight(knights_config["lancelot"])
    lancelot.battle_preparation()
    arthur = Knight(knights_config["arthur"])
    arthur.battle_preparation()
    mordred = Knight(knights_config["mordred"])
    mordred.battle_preparation()
    red_knight = Knight(knights_config["red_knight"])
    red_knight.battle_preparation()

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights))
