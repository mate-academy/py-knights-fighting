from app.participants import KNIGHTS
from app.preparations.knight_stats import Knight
from app.battles.fight import Fight


def battle(list_of_knights: dict) -> dict:

    participants = {}

    # Preparations: equipping armour, weapons and drinking potions
    for knight in list_of_knights.values():
        knight_instance = Knight(
            power=knight["power"],
            health=knight["hp"]
        )

        Knight.armour_on(knight_instance, knight["armour"])
        Knight.weapons_up(knight_instance, knight["weapon"])

        if knight["potion"] is not None:
            Knight.potion_in(knight_instance, knight["potion"]["effect"])

        participants[knight["name"]] = knight_instance

    # Two battles
    Fight.battle(participants["Lancelot"], participants["Mordred"])
    Fight.battle(participants["Artur"], participants["Red Knight"])

    # Tournament results
    return {
        knight_name: knight.hp
        for knight_name, knight in participants.items()
    }


print(battle(KNIGHTS))
