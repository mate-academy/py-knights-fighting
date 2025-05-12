def battle(config: dict) -> dict:

    def prepare(knight: dict) -> dict:
        knight["protection"] = sum(p["protection"] for p in knight["armour"])
        knight["power"] += knight["weapon"]["power"]
        potion = knight.get("potion")
        if potion:
            effects = potion["effect"]
            knight["power"] += effects.get("power", 0)
            knight["hp"] += effects.get("hp", 0)
            knight["protection"] += effects.get("protection", 0)
        return knight

    def fight(knight1: dict, knight2: dict) -> None:
        damage1 = max(0, knight2["power"] - knight1["protection"])
        damage2 = max(0, knight1["power"] - knight2["protection"])

        knight1["hp"] -= damage1
        knight2["hp"] -= damage2

        knight1["hp"] = max(knight1["hp"], 0)
        knight2["hp"] = max(knight2["hp"], 0)

    lancelot = prepare(config["lancelot"])
    arthur = prepare(config["arthur"])
    mordred = prepare(config["mordred"])
    red_knight = prepare(config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
