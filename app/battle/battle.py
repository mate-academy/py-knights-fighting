def fight(knights_data: dict) -> dict:
    result = {}
    knights_list = list(knights_data.values())
    for knight in range(0, len(knights_list) // 2):
        first_knight = knights_list[knight]
        second_knight = knights_list[knight + 2]
        first_knight["hp"] = max(0, first_knight["hp"]
                                 - (second_knight["power"]
                                    - first_knight["protection"]))
        second_knight["hp"] = max(0, second_knight["hp"]
                                  - (first_knight["power"]
                                     - second_knight["protection"]))
        result.update(
            {
                first_knight["name"]: first_knight["hp"],
                second_knight["name"]: second_knight["hp"]
            }
        )
    return result
