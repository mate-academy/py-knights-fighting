def apply_potion(fighter: dict) -> dict:
    if fighter["potion"] is not None:
        for element in fighter["potion"]["effect"]:
            fighter[element] += fighter["potion"]["effect"][element]
