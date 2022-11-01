from app.stats.wear_hero import equipment


def check_hp(super_hero: dict) -> None:
    if super_hero["hp"] <= 0:
        super_hero["hp"] = 0


def fight(knightsconfig: dict) -> dict:
    hero = equipment(knightsconfig)
    lancelot = hero["lancelot"]
    mordred = hero["mordred"]
    artur = hero["arthur"]
    red_knight = hero["red_knight"]

    lancelot["hp"] -= (mordred["power"] - lancelot["armour"])
    mordred["hp"] -= lancelot["power"] - mordred["armour"]
    artur["hp"] -= red_knight["power"] - artur["armour"]
    red_knight["hp"] -= artur["power"] - red_knight["armour"]
    check_hp(lancelot), check_hp(mordred)
    check_hp(artur), check_hp(red_knight)

    return {hero[person].get("name"): hero[person].get("hp")
            for person in hero}
