def protection(knight: dict) -> None:
    knight["add_some_abilities"] = armour_sum(knight["armour"])


def armour_sum(armour: dict) -> int:
    return sum([part_of_armour["add_some_abilities"]
                for part_of_armour in armour])
