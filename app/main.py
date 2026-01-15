from app.knights import KNIGHTS


def battle_preparations(knight: dict) -> dict:
    knight["protection"] = 0
    for armor in knight["armour"]:
        knight["protection"] += armor["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        for effect in knight["potion"]["effect"]:
            if effect in knight["potion"]["effect"]:
                knight[effect] += knight["potion"]["effect"][effect]

    return knight


def battle_knights(knight_1: dict, knight_2: dict) -> tuple:
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]
    # check if someone fell in battle
    if knight_1["hp"] <= 0:
        knight_1["hp"] = 0

    if knight_2["hp"] <= 0:
        knight_2["hp"] = 0

    return knight_1, knight_2


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot, arthur, mordred, red_knight = [
        battle_preparations(knights_config[config])
        for config in knights_config
    ]

    # -------------------------------------------------------------------------------
    # BATTLE:
    lancelot, mordred = battle_knights(lancelot, mordred)
    arthur, red_knight = battle_knights(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
