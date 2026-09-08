from app.arena.fights import Arena
from app.knights.knight import create_knight


def battle(knight_config : dict) -> dict :

    knights = create_knight(knight_config)

    lancelot, mordred = Arena.arena_fight(knights["lancelot"],
                                          knights["mordred"])
    arthur, red_knight = Arena.arena_fight(knights["arthur"],
                                           knights["red_knight"])

    Arena.arena_fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in
            [lancelot, mordred, red_knight, arthur]}
