def battle(battlers: dict) -> None:
    # 1 Lancelot vs Mordred:
    battlers["lancelot"]["hp"] -= battlers["mordred"]["power"] - battlers["lancelot"]["protection"]
    battlers["mordred"]["hp"] -= battlers["lancelot"]["power"] - battlers["mordred"]["protection"]

    # 2 Arthur vs Red Knight:
    battlers["arthur"]["hp"] -= battlers["red_knight"]["power"] - battlers["arthur"]["protection"]
    battlers["red_knight"]["hp"] -= battlers["arthur"]["power"] - battlers["red_knight"]["protection"]

    # check if someone fell in battle
    for health in battlers:
        if battlers[health]["hp"] <= 0:
            battlers[health]["hp"] = 0
