from app.knights.knight import Knight
from app.knights.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    list_of_instances = []
    for knight in knights_config:
        knight_details = knights_config[knight]
        instance = Knight(
            name=knight_details["name"],
            hp=knight_details["hp"],
            power=knight_details["power"]
        )

        hp_in_potion = 0
        power_in_weapon = 0
        power_in_potion = 0
        protection_in_armour = 0
        protection_in_potion = 0

        # apply armour
        for part in knight_details["armour"]:
            protection_in_armour += part["protection"]

        # apply weapon
        power_in_weapon += knight_details["weapon"]["power"]

        # apply potion if exist
        if knight_details["potion"]:
            if "power" in knight_details["potion"]["effect"]:
                power_in_potion += knight_details["potion"]["effect"]["power"]

            if "protection" in knight_details["potion"]["effect"]:
                protection_in_potion += (
                    knight_details["potion"]["effect"]["protection"]
                )

            if "hp" in knight_details["potion"]["effect"]:
                hp_in_potion += knight_details["potion"]["effect"]["hp"]

        instance.all_hp(hp_in_potion)
        instance.all_power(power_in_weapon, power_in_potion)
        instance.all_protection(protection_in_armour, protection_in_potion)

        list_of_instances.append(instance)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot = list_of_instances[0]
    mordred = list_of_instances[2]
    lancelot - mordred
    mordred - lancelot

    # 2 Arthur vs Red Knight:
    arthur = list_of_instances[1]
    red_knight = list_of_instances[3]
    arthur - red_knight
    red_knight - arthur

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
