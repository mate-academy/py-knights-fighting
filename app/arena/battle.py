def duel(knight):
    mordred_dmg = knight["mordred"]["power"] - knight["lancelot"]["protection"]
    lance_dmg = knight["lancelot"]["power"] - knight["mordred"]["protection"]
    knight["lancelot"]["hp"] -= mordred_dmg
    knight["mordred"]["hp"] -= lance_dmg

    # check if someone fell in battle
    if knight["lancelot"]["hp"] <= 0:
        knight["lancelot"]["hp"] = 0

    if knight["mordred"]["hp"] <= 0:
        knight["mordred"]["hp"] = 0

    # 2 Arthur vs Red Knight:
    red_k_dmg = knight["red_knight"]["power"] - knight["arthur"]["protection"]
    arthur_dmg = knight["arthur"]["power"] - knight["red_knight"]["protection"]
    knight["arthur"]["hp"] -= red_k_dmg
    knight["red_knight"]["hp"] -= arthur_dmg

    # check if someone fell in battle
    if knight["arthur"]["hp"] <= 0:
        knight["arthur"]["hp"] = 0

    if knight["red_knight"]["hp"] <= 0:
        knight["red_knight"]["hp"] = 0

    return knight
