from app.participants.lancelot import lancelot
from app.participants.arthur import arthur
from app.participants.mordred import mordred
from app.participants.red_knight import red_knight
from app.knight import Knight
from app.fight import fight


def battle(knights: dict = None) -> dict:
    if knights is None:
        lancelot_conf = Knight(lancelot["lancelot"])
        mordred_conf = Knight(mordred["mordred"])
        arthur_conf = Knight(arthur["arthur"])
        red_knight_conf = Knight(red_knight["red_knight"])
    else:
        lancelot_conf = Knight(knights["lancelot"])
        mordred_conf = Knight(knights["mordred"])
        arthur_conf = Knight(knights["arthur"])
        red_knight_conf = Knight(knights["red_knight"])

    first_fight = fight(lancelot_conf, mordred_conf)
    second_fight = fight(arthur_conf, red_knight_conf)

    return {**first_fight, **second_fight}


if __name__ == "__main__":
    print(battle())
