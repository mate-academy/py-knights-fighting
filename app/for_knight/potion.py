def apply_potion(fighter: list[dict]) -> None:
    if fighter["potion"] is not None:
        for element in fighter["potion"]["effect"]:
            fighter[element] += fighter["potion"]["effect"][element]
