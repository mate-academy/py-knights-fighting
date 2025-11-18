from .knights import Knight

def battle(knights_config: dict) -> dict:
    knights = {name: Knight(cfg) for name, cfg in knights_config.items()}

    for knight in knights.values():
        knight.prepare_for_battle()

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {
        cfg["name"]: knights[key].hp
        for key, cfg in knights_config.items()
    }
