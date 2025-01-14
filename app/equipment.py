from typing import Dict


def create_weapon(name: str, power: int) -> Dict[str, int]:
    """
    Create a weapon with a given name and power.

    :param name: The name of the weapon.
    :param power: The attack power of the weapon.
    :return: A dictionary representing the weapon.
    """
    return {"name": name, "power": power}


def create_armour(part: str, protection: int) -> Dict[str, int]:
    """
    Create an armour piece with a given part name and protection value.

    :param part: The part of the armour (e.g., helmet, boots).
    :param protection: The protection value of the armour.
    :return: A dictionary representing the armour piece.
    """
    return {"part": part, "protection": protection}
