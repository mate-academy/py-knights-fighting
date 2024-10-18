def add_ability_from_potion(knight: dict, ability: str) -> None:
    if ability in knight["potion"]["effect"]:
        knight[ability] += knight["potion"]["effect"][ability]
