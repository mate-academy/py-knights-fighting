from app.knights_info.knights import Knight


def summon_knights(knights_config: dict) -> dict:
    knights = {}
    for knight_name, knight_info in knights_config.items():
        knights[knight_name] = Knight(knight_info["name"],
                                      knight_info["power"],
                                      knight_info["hp"],
                                      knight_info["armour"],
                                      knight_info["weapon"],
                                      knight_info["potion"])
    return knights


def battle(knights_config: dict) -> dict:
    knights = summon_knights(knights_config)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    # battle
    lancelot.battle(mordred)
    arthur.battle(red_knight)

    return {character.name: character.hp
            for character in [lancelot, arthur, mordred, red_knight]}
