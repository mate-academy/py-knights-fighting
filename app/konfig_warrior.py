def sort_through_armour(armors: list[dict]) -> int:
    counter = 0
    for armor in armors:
        counter += armor["protection"]
    return counter


def sort_weapon(power: dict) -> int:
    return power["power"]


def sort_the_potion(potions: dict,
                    power: int,
                    hp: int,
                    protection: int) -> list:
    for key, value in potions.items():
        if key == "power":
            power += value
        if key == "hp":
            hp += value
        if key == "protection":
            protection += value
    return [power, hp, protection]
