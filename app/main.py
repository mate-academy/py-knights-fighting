from knights_date import KNIGHTS


def knights_preparations(knights: KNIGHTS) -> None:
    # BATTLE PREPARATIONS:

    for knight in knights.values():

        # apply armour
        knight["protection"] = sum([armor["protection"]
                                    for armor in knight["armour"]])

        # apply weapon
        knight["power"] += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"]:
            effects = knight["potion"]["effect"]
            knight["power"] += effects.get("power", 0)
            knight["hp"] += effects.get("hp", 0)
            knight["protection"] += effects.get("protection", 0)


def knights_battle(knight1: dict, knight2: dict) -> dict:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]
    winner = knight1 if knight1["hp"] > knight2["hp"] else knight2
    return winner


def battle_tour() -> None:
    knights_preparations(KNIGHTS)
    knights_list = list(KNIGHTS.values())

    while len(knights_list) > 1:
        next_round = []

        for i in range(0, len(knights_list), 2):
            if i + 1 < len(knights_list):
                winner = knights_battle(knights_list[i], knights_list[i + 1])
                next_round.append(winner)
            else:
                next_round.append(knights_list[i])
        knights_list = next_round
    return knights_list[0]["name"].upper()


print(f"THE BATTLE WINNER IS {battle_tour()}")
