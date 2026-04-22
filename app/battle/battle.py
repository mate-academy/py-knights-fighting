def fight(knights_data: dict) -> None:
    result = {}
    knights_list = list(knights_data.values())
    for skills in range(0, len(knights_list) // 2):
        one_knight = knights_list[skills]
        two_knight = knights_list[skills + 2]
        one_knight["hp"] -= two_knight["power"] - one_knight["protection"]
        two_knight["hp"] -= one_knight["power"] - two_knight["protection"]
        if one_knight["hp"] <= 0:
            one_knight["hp"] = 0
        if two_knight["hp"] <= 0:
            two_knight["hp"] = 0
        result.update(
            {
                one_knight["name"]: one_knight["hp"],
                two_knight["name"]: two_knight["hp"]
            }
        )
    return result
