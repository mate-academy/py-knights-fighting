from app.knights.knight import Knight
from app.knights.describtion import Characteristics
from app.additional_config.wepon import Weapon
from app.additional_config.protection import Armour
from app.additional_config.potion import Potion


def battle(dict_knight: dict) -> dict:
    result_dict = {}

    for knight in dict_knight:
        fighter = Knight(dict_knight[knight]["name"])
        basic_config = Characteristics(dict_knight[knight]["hp"],
                                       dict_knight[knight]["power"])
        weapon = Weapon(dict_knight[knight]["weapon"])
        armour = Armour(dict_knight[knight]["armour"])
        result = basic_config.basic_knights_config(weapon.power_weapon,
                                                   armour.protection_armour)
        result_dict.update({fighter.name: result})

        # apply potion if exist
        if dict_knight[knight]["potion"]:

            if "hp" not in dict_knight[knight]["potion"]["effect"]:
                dict_knight[knight]["potion"]["effect"] = 0
            if "power" not in dict_knight[knight]["potion"]["effect"]:
                dict_knight[knight]["potion"]["effect"]["power"] = 0
            if "protection" not in dict_knight[knight]["potion"]["effect"]:
                dict_knight[knight]["potion"]["effect"]["protection"] = 0

            potion = Potion(dict_knight[knight]["potion"]["effect"]["hp"],
                            dict_knight[knight]["potion"]["effect"]["power"],
                            dict_knight[knight]
                            ["potion"]["effect"]["protection"])

            result_dict[fighter.name]["hp"] += potion.effect_hp
            result_dict[fighter.name]["power"] += potion.effect_power
            result_dict[fighter.name]["protection"] += potion.effect_protection

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    result_dict["Lancelot"]["hp"] -= (result_dict["Mordred"]["power"]
                                      - result_dict["Lancelot"]["protection"])
    result_dict["Mordred"]["hp"] -= (result_dict["Lancelot"]["power"]
                                     - result_dict["Mordred"]["protection"])

    # 2 Artur vs Red Knight
    result_dict["Artur"]["hp"] -= (result_dict["Red Knight"]["power"]
                                   - result_dict["Artur"]["protection"])
    result_dict["Red Knight"]["hp"] -= (result_dict["Artur"]["power"]
                                        - result_dict["Red Knight"]
                                        ["protection"])

    # check if someone fell in battle
    for key in result_dict:
        if result_dict[key]["hp"] <= 0:
            result_dict[key]["hp"] = 0

    return {
        "Lancelot": result_dict["Lancelot"]["hp"],
        "Artur": result_dict["Artur"]["hp"],
        "Mordred": result_dict["Mordred"]["hp"],
        "Red Knight": result_dict["Red Knight"]["hp"]
    }
