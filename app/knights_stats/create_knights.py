from app.knights_stats.set_stats import Knight, Armour, Potion, Weapon


def create_knight(knight: dict) -> Knight:
    knight_stats = Knight(name=knight["name"],
                          power=knight["power"],
                          hp=knight["hp"])

    if knight["armour"]:
        for part in knight["armour"]:
            armour = Armour(armour_part=part["part"],
                            protection=part["protection"])

            knight_stats.apply_armor(armour)
    weapon = Weapon(weapon_name=knight["weapon"]["name"],
                    weapon_power=knight["weapon"]["power"])
    knight_stats.apply_weapon(weapon)
    if knight["potion"]:
        hp = knight["potion"]["effect"].get("hp", 0)
        power = knight["potion"]["effect"].get("power", 0)
        protection = knight["potion"]["effect"].get("protection", 0)

        potion = Potion(name=knight["potion"]["name"],
                        hp=hp,
                        power=power,
                        protection=protection)
        knight_stats.use_potion(potion)
    print("\n------------------\n")
    return knight_stats


def preparations(knights: dict) -> tuple:
    knights_dict = {}
    for person in knights:
        knights_dict[person] = create_knight(knights[person])

    return (knights_dict["lancelot"],
            knights_dict["mordred"],
            knights_dict["arthur"],
            knights_dict["red_knight"])
