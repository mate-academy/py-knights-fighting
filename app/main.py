from app.Knight_database.data import KNIGHTS
from app.Stats.knights import Knight


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:
    contestants = []
    for knight in knights.values():
        contestants.append(Knight(knight))

    print(f'''\nWelcome, ladies and gentlemen at our first grand knight tournament!
Our competitors are two pairs of incredibly skilled knights of the kingdom.
For the first pair we have {contestants[0].name} and {contestants[2].name}
For the second one {contestants[1].name} and {contestants[3].name}
Let's go through the equipment of our fighters while they are preparing.''')

    for knight in contestants:
        knight.ready_for_battle()
    # -------------------------------------------------------------------------------
    # BATTLE
    print("Let the battle begin!")
    contestants[0].hp -= contestants[2].power - contestants[0].prot
    contestants[2].hp -= contestants[0].power - contestants[2].prot
    contestants[1].hp -= contestants[3].power - contestants[1].prot
    contestants[3].hp -= contestants[1].power - contestants[3].prot
    for knight in contestants:
        if knight.hp <= 0:
            knight.hp = 0
            print(f"{knight.name} is dead!")
    return {contestant.name: contestant.hp for contestant in contestants}


print(battle(KNIGHTS))
