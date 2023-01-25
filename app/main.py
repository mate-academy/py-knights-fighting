from app.participants import KNIGHTS
from app.preparations.knight_stats import Knight
from app.preparations.putting_equip_on import Equipment
from app.battles.fight import Fight
from app.battles.tournament_table import Table


def battle(list_of_knights: dict) -> dict:

    participants = {}

    # Preparations: equipping armour, weapons and drinking potions
    for knight in list_of_knights.values():
        the_knight = Knight(
            power=knight["power"],
            health=knight["hp"]
        )

        Equipment.armour_on(the_knight, knight["armour"])
        Equipment.weapons_up(the_knight, knight["weapon"])

        if knight["potion"] is not None:
            Equipment.potion_in(the_knight, knight["potion"]["effect"])

        participants[knight["name"]] = the_knight

    # Two battles
    Fight.battle(participants["Lancelot"], participants["Mordred"])
    Fight.battle(participants["Artur"], participants["Red Knight"])

    # Tournament results
    return Table.results(participants=participants)


# main battle: {'Lancelot': 0, 'Artur': 30, 'Mordred': 35, 'Red Knight': 5}
print(battle(KNIGHTS))
