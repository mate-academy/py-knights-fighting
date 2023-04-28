def combat(combatants: dict, name1: str, name2: str) -> None:
    combatants[name1]["hp"] -= (
        combatants[name2]["power"] - combatants[name1]["protection"]
    )
    combatants[name2]["hp"] -= (
        combatants[name1]["power"] - combatants[name2]["protection"]
    )


def fighting(battlers: dict) -> None:
    # 1 Lancelot vs Mordred:
    combat(battlers, "lancelot", "mordred")

    # 2 Arthur vs Red Knight:
    combat(battlers, "arthur", "red_knight")

    # check if someone fell in battle
    for health in battlers:
        if battlers[health]["hp"] <= 0:
            battlers[health]["hp"] = 0
