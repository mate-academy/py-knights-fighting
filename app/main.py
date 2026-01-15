from app.knight_fighting.knight import Knight
from app.knight_fighting.battle import Battle
from app.knight_fighting.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot_dict = knights_config["lancelot"]
    lancelot = Knight(
        name=lancelot_dict["name"],
        power=lancelot_dict["power"],
        hp=lancelot_dict["hp"],
        armour=lancelot_dict["armour"],
        weapon=lancelot_dict["weapon"],
        potion=lancelot_dict["potion"]
    )

    # apply armour, weapon and potion
    lancelot.apply_armour()
    lancelot.apply_weapon()
    lancelot.apply_potion()

    # arthur
    arthur_dict = knights_config["arthur"]
    arthur = Knight(
        name=arthur_dict["name"],
        power=arthur_dict["power"],
        hp=arthur_dict["hp"],
        armour=arthur_dict["armour"],
        weapon=arthur_dict["weapon"],
        potion=arthur_dict["potion"]
    )

    # apply armour, weapon and potion
    arthur.apply_armour()
    arthur.apply_weapon()
    arthur.apply_potion()

    # mordred
    mordred_dict = knights_config["mordred"]
    mordred = Knight(
        name=mordred_dict["name"],
        power=mordred_dict["power"],
        hp=mordred_dict["hp"],
        armour=mordred_dict["armour"],
        weapon=mordred_dict["weapon"],
        potion=mordred_dict["potion"]
    )

    # apply armour, weapon and potion
    mordred.apply_armour()
    mordred.apply_weapon()
    mordred.apply_potion()

    # red_knight
    red_knight_dict = knights_config["red_knight"]
    red_knight = Knight(
        name=red_knight_dict["name"],
        power=red_knight_dict["power"],
        hp=red_knight_dict["hp"],
        armour=red_knight_dict["armour"],
        weapon=red_knight_dict["weapon"],
        potion=red_knight_dict["potion"]
    )

    # apply armour, weapon and potion
    red_knight.apply_armour()
    red_knight.apply_weapon()
    red_knight.apply_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle1 = Battle(lancelot, mordred)
    battle1.simulate_battle()

    # 2 Arthur vs Red Knight:
    battle2 = Battle(arthur, red_knight)
    battle2.simulate_battle()

    # Return battle results:
    print(battle1.get_winner())
    print(battle2.get_winner())
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
