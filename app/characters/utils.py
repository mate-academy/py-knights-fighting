from app.characters.knight import Knight
list_of_actions = ["weapon", "armour", "potion"]


def prepare_knights(
        knights: list[Knight],
        original_knights: dict
) -> None:
    for action in list_of_actions:
        for knight in knights:
            knight_name = knight.name.lower().replace(" ", "_")
            if action == "weapon":
                knight.apply_weapon(original_knights[knight_name][action])
            elif action == "armour":
                knight.apply_armour(original_knights[knight_name][action])
            elif action == "potion":
                if original_knights[knight_name]["potion"] is not None:
                    knight.apply_potion(original_knights[knight_name][action])
