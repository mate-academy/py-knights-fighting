from app.battle.knight_creator import Knight


def members_list(members: dict, member_class: object) -> list:
    output = []
    for i, params in members.items():
        output.append(member_class(params, i))
    return output


def members_sort(elem: Knight) -> int:
    return elem.list_order


def pvp_list(members: list) -> list:
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

    fighter_1, fighter_2 = fighters

    fighter_1.use_potion()
    fighter_2.use_potion()

    fighter_1.defence(fighter_2.attack())
    fighter_2.defence(fighter_1.attack())

    return [fighter_1, fighter_2]
