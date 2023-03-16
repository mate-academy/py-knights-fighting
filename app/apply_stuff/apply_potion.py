def apply_potion(knight: dict) -> None:
    parameters = ["power", "protection", "hp"]

    if knight.get("potion"):
        for parameter in parameters:
            if parameter in knight["potion"]["effect"]:
                knight[parameter] += knight["potion"]["effect"][parameter]
