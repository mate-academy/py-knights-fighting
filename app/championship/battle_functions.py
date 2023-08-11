from app.championship.knights import Knight


def duel(fighter_1: str, fighter_2: str) -> None:
    fighters = [Knight.knights[fighter_1], Knight.knights[fighter_2]]
    fighters[0].hp -= fighters[1].power - fighters[0].protection
    fighters[1].hp -= fighters[0].power - fighters[1].protection
    for fighter in fighters:
        if fighter.hp <= 0:
            fighter.hp = 0


def results(members: dict) -> dict:
    return {member.name: member.hp for member in members.values()}
