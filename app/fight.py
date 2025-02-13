def fight(fighter1: dict, fighter2: dict) -> dict:
    fighter1["hp"] -= fighter2["power"] - fighter1["protection"]
    fighter2["hp"] -= fighter1["power"] - fighter2["protection"]

    fighter1["hp"] = max(fighter1["hp"], 0)
    fighter2["hp"] = max(fighter2["hp"], 0)

    return {
        fighter1["name"]: fighter1["hp"],
        fighter2["name"]: fighter2["hp"],
    }
