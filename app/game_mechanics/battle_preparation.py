from app.npc.knights import fighters
# from app.game_mechanics.dice import modifying
# from app.game_mechanics.dice import rolling

lancelot = fighters["lancelot"]
arthur = fighters["arthur"]
mordred = fighters["mordred"]
red_knight = fighters["red_knight"]
list_of_knights = [lancelot, arthur, mordred, red_knight]


def armour_preparation():

    for i in list_of_knights:
        i["protection"] = i["helmet"] + i["boots"] + i["breastplate"]
        return i


def potion_preparation():

    for i in list_of_knights:

        if i["potion"] is not None:
            i["hp"] = i["hp"] + i["potion_hp"]
            i["power"] = i["power"] + i["potion_power"]
            i["protection"] = i["protection"] + i["potion_protection"]
        return i


def arming():

    for i in list_of_knights:
        i["power"] += i["weapon_power"]
        return i
