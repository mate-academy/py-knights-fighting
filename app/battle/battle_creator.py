from app.battle.knight_creator import Knight


def members_list(members: dict, member_class: object) -> list:
    """
    Creates a list of knights from the dictionary.

    Args:
    - members (dict): Dictionary of knight parameters
    - member_class (object): The class of the knight to be created.

    Returns:
    - list: List of created knights.
    """
    output = []

    for i, (nik, params) in enumerate(members.items()):
        output.append(member_class(nik, params, i))
    return output


def members_sort(elem: Knight) -> int:
    """
    Sorts a list of knights by their list_order attribute.

    Args:
    - elem (Knight): A knight object

    Returns:
    - int: The value of the knight's list_order attribute.
    """
    return elem.list_order


def pvp_list(members: list) -> list:
    """
    Creates a list of pairs of knights from a list.

    Args:
    - members (list): A list of knights.

    Returns:
    - list: A list of lists, each containing two knights.
    """
    output = []

    if len(members) % 2 != 0:
        del members[len(members) - 1]

    odd = [members[i] for i in range(len(members)) if i % 2 == 0]
    even = [members[i] for i in range(len(members)) if i % 2 != 0]

    for i in range(0, len(odd), 2):
        if i + 2 <= len(odd):
            output.append([odd[i], odd[i + 1]])
            output.append([even[i], even[i + 1]])
        else:
            output.append([odd[i], even[i]])

    return output


def pvp_battle(fighters: list[Knight]) -> list:
    """
    Simulates a single PvP battle between two knights.

    Args:
    - fighters (list): A list of two knights.

    Returns:
    - list: A list of two knights with their updated HP values.
    """
    fighter_1, fighter_2 = fighters

    fighter_1.use_potion()
    fighter_2.use_potion()

    fighter_1.defence(fighter_2.attack())
    fighter_2.defence(fighter_1.attack())

    return [fighter_1, fighter_2]
