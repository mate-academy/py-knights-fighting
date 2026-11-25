from app.knight import Knight


def battle(all_targets: dict) -> dict:
    knight_list = []
    for knight in all_targets.values():
        knight_list.append(
            Knight(
                knight["name"],
                knight["power"],
                knight["hp"],
                knight["armour"],
                knight["weapon"],
                knight["potion"]
            )
        )
    fight(knight_list[0], knight_list[2])
    fight(knight_list[1], knight_list[3])
    return {
        knight_list[0].name : knight_list[0].hp,
        knight_list[1].name : knight_list[1].hp,
        knight_list[2].name : knight_list[2].hp,
        knight_list[3].name : knight_list[3].hp,
    }


def fight(first: Knight, second: Knight) -> None:
    first.battle_prep()
    second.battle_prep()

    first.hp = (
        first.battle_hp
        - (second.battle_power - first.battle_protection)
    )

    second.hp = (
        second.battle_hp
        - (first.battle_power - second.battle_protection)
    )

    if first.hp <= 0:
        first.hp = 0

    if second.hp <= 0:
        second.hp = 0
