from app.knights import KNIGHTS


def apply_effects(character: dict, effects: dict) -> None:
    if "power" in effects:
        character["power"] += effects["power"]
    if "protection" in effects:
        character["protection"] += effects["protection"]
    if "hp" in effects:
        character["hp"] += effects["hp"]


def prepare_knight(knight: dict) -> None:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"] is not None:
        apply_effects(knight, knight["potion"]["effect"])


def battle(knights_config: dict) -> dict:
    knights = ["lancelot", "arthur", "mordred", "red_knight"]

    for knight_name in knights:
        knight = knights_config[knight_name]
        prepare_knight(knight)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in [lancelot, mordred, arthur, red_knight]:
        knight["hp"] = max(knight["hp"], 0)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
