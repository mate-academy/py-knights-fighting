def create_knight(config: dict):
    name = config["name"]
    hp = config["hp"]
    power = config["power"] + config["weapon"]["power"]
    protection = sum(armour["protection"] for armour in config.get("armour", []))

    potion = config.get("potion")
    if potion:
        effects = potion.get("effect", {})
        hp += effects.get("hp", 0)
        power += effects.get("power", 0)
        protection += effects.get("protection", 0)

    from app.models import Knight
    return Knight(name, hp, power, protection)