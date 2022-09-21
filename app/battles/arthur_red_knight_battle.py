def arthur_red_knight_battle(arthur: dict, red_knight: dict) -> tuple:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    print("--------------------------------")
    if arthur["hp"] <= 0:
        arthur["hp"] = 0
        print("And the winner is... Red Knight!")
    elif red_knight["hp"] <= 0:
        red_knight["hp"] = 0
        print("And the winner is... Arthur!")
    else:
        print("And the winner is... No one won.")

    return arthur, red_knight
