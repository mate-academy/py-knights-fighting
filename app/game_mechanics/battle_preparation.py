from app.npc.knights import fighters
# from app.game_mechanics.dice import modifying
# from app.game_mechanics.dice import rolling

lancelot = fighters["lancelot"]
arthur = fighters["arthur"]
mordred = fighters["mordred"]
red_knight = fighters["red_knight"]
list_of_knights = [lancelot, arthur, mordred, red_knight]


def armour_preparation():

    for knight in list_of_knights:
        knight["protection"] = knight["helmet"] + knight["boots"] + knight["breastplate"]
        return knight


def potion_preparation():

    for knight in list_of_knights:

        if knight["potion"] is not None:
            knight["hp"] = knight["hp"] + knight["potion_hp"]
            knight["power"] = knight["power"] + knight["potion_power"]
            knight["protection"] = knight["protection"] + knight["potion_protection"]
        return knight


def arming():

    for knight in list_of_knights:
        knight["power"] += knight["weapon_power"]
        return knight
