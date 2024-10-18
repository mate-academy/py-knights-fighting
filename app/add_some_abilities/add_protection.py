def protection(knight: dict) -> None:
    knight["add_some_abilities"] = sum(
        [part_of_armour["add_some_abilities"]
         for part_of_armour in knight["armour"]])
