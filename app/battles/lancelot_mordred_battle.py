def lancelot_mordred_battle(lancelot: dict, mordred: dict) -> tuple:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    print("--------------------------------")
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0
        print("And the winner is... Mordred!")
    elif mordred["hp"] <= 0:
        mordred["hp"] = 0
        print("And the winner is... Lancelot!")
    else:
        print("And the winner is... No one won.")

    return lancelot, mordred
