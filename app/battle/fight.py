from app.preparation.create_knight import Knight


def battle(battlers: list[Knight]) -> None:

    # 1 Lancelot vs Mordred:
    battlers[0].hp -= battlers[2].power - battlers[0].protection
    battlers[2].hp -= battlers[0].power - battlers[2].protection

    # 2 Arthur vs Red Knight:
    battlers[1].hp -= battlers[3].power - battlers[1].protection
    battlers[3].hp -= battlers[1].power - battlers[3].protection

    # check if someone fell in battle
    for health in battlers:
        if health.hp <= 0:
            health.hp = 0
