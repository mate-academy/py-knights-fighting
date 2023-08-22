from app.KNIGHTS.KnightsInfo import KNIGHTS
from app.KNIGHTS.ReformattingInfo import making_knight


def battle(knights_config: dict) -> dict:
    # Reformatting info about the Knights
    knights_names = ["lancelot", "mordred", "arthur", "red_knight"]

    knights = [making_knight(knights_config[knight]) for knight in knights_names]

# BATTLE------------------------------------------------

    # 1 Lancelot vs Mordred:

    knights[0].hp -= knights[1].power - knights[0].protection
    knights[1].hp -= knights[0].power - knights[1].protection

    # 2 Arthur vs Red Knight:

    knights[2].hp -= knights[3].power - knights[2].protection
    knights[3].hp -= knights[2].power - knights[3].protection

    # check if someone fell in battle

    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0

    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp,
    }


print(battle(KNIGHTS))
