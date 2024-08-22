from app.warrior.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {}
    for data in knights_config.values():
        knight = Knight(**data)
        knight.get_ready_to_battle()
        knights.update({data["name"]: knight})

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    knights["Lancelot"].fight(knights["Mordred"])

    # 2 Arthur vs Red Knight:
    knights["Arthur"].fight(knights["Red Knight"])

    return {knight.name: knight.hp for knight in knights.values()}
