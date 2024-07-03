# Test your might knight!!!
def fight(knight1, knight2):
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    # Ensure HP does not go below 0
    if knight1["hp"] <= 0:
        knight1["hp"] = 0
    if knight2["hp"] <= 0:
        knight2["hp"] = 0
