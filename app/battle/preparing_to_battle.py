from app.gladiators.create_gladiator import create_gladiator


def preparing_to_battle(knights_config: dict) -> dict:


    gladiators = create_gladiator(knights_config)
    for gladiator in gladiators.values():
        if gladiator.armour:
            for armour in gladiator.armour:
                gladiator.protection += armour["protection"]
        gladiator.power += gladiator.weapon["power"]
        if gladiator.potion is not None:
            if "power" in gladiator.potion["effect"]:
                gladiator.power += gladiator.potion["effect"]["power"]

            if "protection" in gladiator.potion["effect"]:
                gladiator.protection += (
                    gladiator.potion)["effect"]["protection"]

            if "hp" in gladiator.potion["effect"]:
                gladiator.hp += gladiator.potion["effect"]["hp"]
    return gladiators
