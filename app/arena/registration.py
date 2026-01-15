from app.arena.calc_stats import KnightStat


def registration(KNIGHTS):
    res = {}
    for key, value in KNIGHTS.items():
        knight = KnightStat(value)
        res[key] = knight.calc_stats()
    return res
