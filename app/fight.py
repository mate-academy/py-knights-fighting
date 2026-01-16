from app.knights import Knights


def fight(knights_config: dict) -> list:
    knight_instances = []
    for player, info in knights_config.items():
        name, power, hp, armours, weapons, potion = info.values()

        knight_instance = Knights(
            name=name,
            power=power,
            hp=hp
        )
        if armours:
            protection = []
            for armour in armours:
                protection.append(armour["protection"])
            knight_instance.get_protection(protection)

        knight_instance.get_power(weapons["power"])

        if potion:
            if "power" in potion["effect"]:
                knight_instance.get_power(potion["effect"]["power"])
            if "hp" in potion["effect"]:
                knight_instance.get_hp(potion["effect"]["hp"])
            if "protection" in potion["effect"]:
                knight_instance.get_protection(potion["effect"]["protection"])
        knight_instances.append(knight_instance)

    return knight_instances
