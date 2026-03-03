from app.knights.knights import Knight


def creating_knight(name: str, knights_config: dict) -> Knight:
    config = knights_config[name]
    new_knight = Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"]
    )
    new_knight.apply_armour(armour=config["armour"])
    new_knight.apply_weapon(weapon=config["weapon"])
    new_knight.apply_potion(potion=config["potion"])
    new_knight.add_armour_protection()
    new_knight.add_weapon_power()
    new_knight.add_potion_effects()
    return new_knight
