from app.knight import Knights
from app.knights_stats.lancelot_stats import LANCELOT
from app.knights_stats.arthur_stats import ARTHUR
from app.knights_stats.mordred_stats import MORDRED
from app.knights_stats.red_knight_stats import RED_KNIGHT


def battle(config: dict) -> dict:
    knights = {key: Knights.from_dict(config[key]) for key in config}

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


def fight(knight1: Knights, knight2: Knights) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    check_defeat(knight1)
    check_defeat(knight2)


def check_defeat(knight: Knights) -> None:
    if knight.hp <= 0:
        knight.hp = 0


config = {
    "lancelot": LANCELOT["lancelot"],
    "arthur": ARTHUR["arthur"],
    "mordred": MORDRED["mordred"],
    "red_knight": RED_KNIGHT["red_knight"],
}

print(battle(config))
