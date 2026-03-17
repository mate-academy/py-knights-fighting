from app.knights.basic_stats import Knight
from app.knights.prepared_knight import knight_from_dict
from app.battle.fight import fight


def build_knight(config: dict, key: str) -> Knight:
    return knight_from_dict(config[key])


def battle(config: dict) -> dict[str, int]:
    order = ["lancelot", "arthur", "mordred", "red_knight"]

    knights = {key: knight_from_dict(config[key]) for key in order}

    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for first, second in pairs:
        fight(knights[first], knights[second])

    return {knights[k].name: knights[k].hp for k in order}
