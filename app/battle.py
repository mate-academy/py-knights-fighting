from app.functions import check_hp, apply_potion


def battle(knights_config: dict) -> dict:
    for name, knight in knights_config.items():
        # BATTLE PREPARATIONS:
        name = knights_config[name]

        # apply potion
        apply_potion(list(knights_config.keys()), name)

    # BATTLE:
    def do_battle(knight1: dict, knight2: dict) -> None:
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]
        knight1["hp"] = check_hp(knight1["hp"])
        knight2["hp"] = check_hp(knight2["hp"])

    # Battle 1: Lancelot vs Mordred
    do_battle(knights_config["lancelot"], knights_config["mordred"])

    # Battle 2: Arthur vs Red Knight
    do_battle(knights_config["arthur"], knights_config["red_knight"])

    return {f"{knight_name}".replace("_", " ").title(): config["hp"]
            for knight_name, config in knights_config.items()}
