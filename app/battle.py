from app.functions import check_hp, apply_potion


def battle(knights_config: dict) -> dict:
    knights_list = [*knights_config.keys()]

    for knight in range(len(knights_list)):
        # BATTLE PREPARATIONS:
        knights_list[knight] = knights_config[knights_list[knight]]

        # apply potion
        apply_potion(knights_list, knight)

    # BATTLE:
    def do_battle(knight1: str, knight2: str) -> None:
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]
        knight1["hp"] = check_hp(knight1["hp"])
        knight2["hp"] = check_hp(knight2["hp"])

    # Battle 1: Lancelot vs Mordred
    do_battle(knights_list[0], knights_list[2])

    # Battle 2: Arthur vs Red Knight
    do_battle(knights_list[1], knights_list[3])

    return {
        knights_list[0]["name"]: knights_list[0]["hp"],
        knights_list[1]["name"]: knights_list[1]["hp"],
        knights_list[2]["name"]: knights_list[2]["hp"],
        knights_list[3]["name"]: knights_list[3]["hp"],
    }
