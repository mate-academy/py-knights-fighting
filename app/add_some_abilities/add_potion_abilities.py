def add_ability_from_potion(knight: dict, ability: str) -> None:
    if check_presence_ability(knight, ability):
        knight[ability] += knight["potion"]["effect"].get(ability)


def check_presence_ability(knight: dict, ability: str) -> bool:
    if ability in knight["potion"]["effect"]:
        return True
    return False
