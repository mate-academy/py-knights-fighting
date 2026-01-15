def fights(fighter1: dict, fighter2: dict) -> None:
    fighter1["hp"] -= \
        (fighter2["power"] - fighter1["protection"])
    fighter2["hp"] -= \
        (fighter1["power"] - fighter2["protection"])
