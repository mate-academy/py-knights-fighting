from app.people.knights import Knight


def make_participants_list(participants: dict) -> dict:
    participants_list = {}
    for knight_name, knight_data in participants.items():
        knight = Knight(
            name=knight_data.get("name"),
            power=knight_data.get("power"),
            hp=knight_data.get("hp"),
            armour=knight_data.get("armour"),
            weapon=knight_data.get("weapon"),
            potion=knight_data.get("potion"),
        )
        participants_list[knight.name] = knight

    return participants_list


def make_pairs(participants_list: dict) -> list:
    pairs_list = []
    participants = make_participants_list(participants_list)
    pairs_list.append((participants["Lancelot"], participants["Mordred"]))
    pairs_list.append((participants["Artur"], participants["Red Knight"]))

    return pairs_list
