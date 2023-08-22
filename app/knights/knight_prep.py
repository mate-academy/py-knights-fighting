from app.knights.create_knight import CreateKnight
list_of_actions = ["weapon", "armour", "potion"]


def knight_preparation(
        list_of_knights: list[CreateKnight],
        dict_of_knights: dict
) -> None:
    for action in list_of_actions:
        for knight in list_of_knights:
            knight_name = knight.name.lower().replace(" ", "_")
            if action == "weapon":
                knight.apply_weapon(dict_of_knights[knight_name][action])
            elif action == "armour":
                knight.apply_armour(dict_of_knights[knight_name][action])
            elif action == "potion":
                if dict_of_knights[knight_name]["potion"] is not None:
                    knight.apply_potion(dict_of_knights[knight_name][action])
