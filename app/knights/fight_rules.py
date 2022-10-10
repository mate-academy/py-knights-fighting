from app.knights.class_of_knigts import Knights


def main_battle(knight: Knights, another: Knights) -> type(None):
    knight.hp -= another.power - knight.protection
    another.hp -= knight.power - another.protection

    if knight.hp <= 0:
        knight.hp = 0

    if another.hp <= 0:
        another.hp = 0


def battle_to_death(knight: Knights, another: Knights) -> Knights or str:
    deaths = 0
    while deaths == 0:
        knight.hp -= another.power - knight.protection
        another.hp -= knight.power - another.protection

        if knight.hp <= 0:
            knight.hp = 0
            deaths += 1

        if another.hp <= 0:
            another.hp = 0
            deaths += 1
    if deaths == 2:
        print(f"{knight.name} and {another.name} are defeated!")
        return "Draw"
    if another.hp == 0:
        print(f"{another.name} is defeated in a fair fight!")
        print(f"{knight.name} wins")
        return knight
    if knight.hp == 0:
        print(f"{knight.name} is defeated in a fair fight!")
        print(f"{another.name} wins")
        return another


def championship(members: list) -> type(None):
    finalists = [
        members[i].battle_to_death(members[i + 1])
        for i in range(0, len(members), 2)
    ]
    winner = finalists[0].battle_to_death(finalists[1])
    if winner == "Draw":
        print("All knights is dead")
        print("It was beautiful and spectacular championship")
    else:
        print(f"winner of championship is {winner.name}!")
