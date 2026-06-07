def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights_keys = []
    for knight in knights_config:
        knights_keys.append(knight)
    # For declared knights
    knights = {}
    for key in knights_keys:
        # Declare knight
        knight = knights_config.get(key)
        # apply armour
        knight["protection"] = 0
        for arm in knight["armour"]:
            knight["protection"] += arm["protection"]
        # apply weapon
        knight["power"] += knight["weapon"]["power"]
        # apply potion if exist
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += knight["potion"]["effect"][
                    "protection"
                ]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
        knights[key] = knight
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights[knights_keys[0]]["hp"] -= (
        knights[knights_keys[2]]["power"]
        - knights[knights_keys[0]]["protection"]
    )
    knights[knights_keys[2]]["hp"] -= (
        knights[knights_keys[0]]["power"]
        - knights[knights_keys[2]]["protection"]
    )

    # check if someone fell in battle
    check_if_someone_fell(
        knights_keys=knights_keys, knights=knights, number_of_battle=1
    )

    # 2 Arthur vs Red Knight:
    knights[knights_keys[1]]["hp"] -= (
        knights[knights_keys[3]]["power"]
        - knights[knights_keys[1]]["protection"]
    )
    knights[knights_keys[3]]["hp"] -= (
        knights[knights_keys[1]]["power"]
        - knights[knights_keys[3]]["protection"]
    )

    # check if someone fell in battle
    check_if_someone_fell(
        knights_keys=knights_keys, knights=knights, number_of_battle=2
    )

    # Return battle results:
    return {
        knights[knights_keys[i]]["name"]: knights[knights_keys[i]]["hp"]
        for i in range(len(knights_keys))
    }


def check_if_someone_fell(
    knights_keys: list, knights: dict, number_of_battle: int
) -> None:
    if number_of_battle == 1:
        if knights[knights_keys[0]]["hp"] <= 0:
            knights[knights_keys[0]]["hp"] = 0
        if knights[knights_keys[2]]["hp"] <= 0:
            knights[knights_keys[2]]["hp"] = 0
    else:
        if knights[knights_keys[1]]["hp"] <= 0:
            knights[knights_keys[1]]["hp"] = 0
        if knights[knights_keys[3]]["hp"] <= 0:
            knights[knights_keys[3]]["hp"] = 0
