def sort_through_armour(armors: list[dict]) -> int:
    summa = 0
    for armor in armors:
        summa += armor["protection"]
    return summa


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
