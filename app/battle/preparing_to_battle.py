from app.gladiators.create_gladiator import create_gladiator


def preparing_to_battle(knightsconfig: dict) -> dict:

    # BATTLE PREPARATIONS:
    # Creating gladiators:
    gladiators = create_gladiator(knightsconfig)
    # gladiator
    for gladiator_obj in gladiators:
        gladiator = gladiators[gladiator_obj]
    # apply armour
        gladiator.protection = 0
        if gladiator.armour:
            for armour in gladiator.armour:
                gladiator.protection += armour["protection"]
        # apply weapon
        gladiator.power += gladiator.weapon["power"]
        # apply potion if exist
        if gladiator.potion is not None:
            if "power" in gladiator.potion["effect"]:
                gladiator.power += gladiator.potion["effect"]["power"]

            if "protection" in gladiator.potion["effect"]:
                gladiator.protection += (
                    gladiator.potion)["effect"]["protection"]

            if "hp" in gladiator.potion["effect"]:
                gladiator.hp += gladiator.potion["effect"]["hp"]
    return gladiators
