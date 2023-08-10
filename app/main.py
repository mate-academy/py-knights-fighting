from app.Fighters.Knights_info import fill_knight_info


def fighting(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    # check if someone fell in battle
    knight1["hp"] = 0 if knight1["hp"] <= 0 else knight1["hp"]
    knight2["hp"] = 0 if knight2["hp"] <= 0 else knight2["hp"]


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = fill_knight_info(knights_config["lancelot"])

    # arthur
    arthur = fill_knight_info(knights_config["arthur"])

    # mordred
    mordred = fill_knight_info(knights_config["mordred"])

    # red_knight
    red_knight = fill_knight_info(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fighting(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fighting(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
