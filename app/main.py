from app.Battle.Fight import fight
from app.knights.Create_Knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(
        knights["lancelot"]["name"],
        knights["lancelot"]["power"],
        knights["lancelot"]["hp"]
    )
    arthur = Knight(
        knights["arthur"]["name"],
        knights["arthur"]["power"],
        knights["arthur"]["hp"]
    )
    mordred = Knight(
        knights["mordred"]["name"],
        knights["mordred"]["power"],
        knights["mordred"]["hp"]
    )
    red_knight = Knight(
        knights["red_knight"]["name"],
        knights["red_knight"]["power"],
        knights["red_knight"]["hp"]
    )

    list_of_knights = [lancelot, arthur, mordred, red_knight]
    list_of_actions = ["weapon", "armour", "potion"]

    for action in list_of_actions:
        for knight in list_of_knights:
            knight_name = knight.name.lower().replace(" ", "_")
            if action == "weapon":
                knight.apply_weapon(knights[knight_name][action])
            elif action == "armour":
                knight.apply_armour(knights[knight_name][action])
            elif action == "potion":
                if knights[knight_name]["potion"] is not None:
                    knight.apply_potion(knights[knight_name][action])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        "Arthur": arthur.hp,
        "Lancelot": lancelot.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp
    }
