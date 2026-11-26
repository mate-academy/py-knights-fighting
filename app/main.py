from app.knight import Knight


def battle(all_targets: dict) -> dict:
    knights = {}
    for knight in all_targets.values():
        knights[knight["name"]] = (
            Knight(
                knight["name"],
                knight["power"],
                knight["hp"],
                knight["armour"],
                knight["weapon"],
                knight["potion"]
            )
        )
    fight(knights["Lancelot"], knights["Mordred"])
    fight(knights["Arthur"], knights["Red Knight"])
    return {
        knights["Lancelot"].name : knights["Lancelot"].hp,
        knights["Arthur"].name : knights["Arthur"].hp,
        knights["Mordred"].name : knights["Mordred"].hp,
        knights["Red Knight"].name : knights["Red Knight"].hp,
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
