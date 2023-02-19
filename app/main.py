from app.hall.fighters import Fighters
from app.arena.preparation import Prepare
from app.arena.fight import Battle


def battle(knights: list) -> dict:
    fighters_list = []
    result = {}

    for key, value in knights.items():
        locals()[key] = Fighters(
            value["name"],
            value["power"],
            value["hp"],
            value["armour"],
            value["weapon"],
            value["potion"]
        )

        Prepare.armour_prepare(locals()[key])
        Prepare.weapon_prepare(locals()[key])
        Prepare.potion_prepare(locals()[key])

        fighters_list.append(locals()[key])

    for fighter_1 in fighters_list:

        for fighter_2 in fighters_list:
            if fighter_1.name == "Lancelot" and fighter_2.name == "Mordred":
                Battle.fight(fighter_1, fighter_2)
            elif fighter_1.name == "Artur" and fighter_2.name == "Red Knight":
                Battle.fight(fighter_1, fighter_2)

        result[fighter_1.name] = fighter_1.hp

    return result
