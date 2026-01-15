import time

from app.Knight.knight import Knight


def create_knights(knight_stats: dict) -> dict:
    knights = {}
    lancelot_stats = knight_stats.get("lancelot")
    lancelot = Knight(
        name=lancelot_stats.get("name"),
        power=lancelot_stats.get("power"),
        hp=lancelot_stats.get("hp"),
    )
    knights["lancelot"] = [lancelot, lancelot_stats]

    arthur_stats = knight_stats.get("arthur")
    arthur = Knight(
        name=arthur_stats.get("name"),
        power=arthur_stats.get("power"),
        hp=arthur_stats.get("hp")
    )
    knights["arthur"] = [arthur, arthur_stats]

    mordred_stats = knight_stats.get("mordred")
    mordred = Knight(
        name=mordred_stats.get("name"),
        power=mordred_stats.get("power"),
        hp=mordred_stats.get("hp")
    )
    knights["mordred"] = [mordred, mordred_stats]

    red_knight_stats = knight_stats.get("red_knight")
    red_knight = Knight(
        name=red_knight_stats.get("name"),
        power=red_knight_stats.get("power"),
        hp=red_knight_stats.get("hp")
    )
    knights["red_knight"] = [red_knight, red_knight_stats]
    return knights


def battle(knight_stats: dict[dict]) -> dict:

    knights = create_knights(knight_stats)
    for knight in knights.values():
        knight[0].equip_knight(
            armour=knight[1].get("armour"),
            weapon=knight[1].get("weapon"),
            potion=knight[1].get("potion")
        )

    lancelot = knights.get("lancelot")[0]
    arthur = knights.get("arthur")[0]
    mordred = knights.get("mordred")[0]
    red_knight = knights.get("red_knight")[0]

    print("-----------Lancelot vs Mordred----------")
    time.sleep(0.5)
    lancelot_vs_mordred_result = lancelot.battle_between_two(mordred)
    time.sleep(0.5)
    print("----------Arthur vs Red Knight----------")
    arthur_vs_red_knight_result = arthur.battle_between_two(red_knight)
    time.sleep(0.5)
    print("---------       Result      -----------")
    return {**lancelot_vs_mordred_result, **arthur_vs_red_knight_result}
