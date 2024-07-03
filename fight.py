# Test your might knight!!!
def apply_damage(attacker, defender):
    defender["hp"] -= max(0, attacker["power"] - defender["protection"])
    # ensure that hp isn't below 0
    if defender["hp"] < 0:
        defender["hp"] = 0


def fight(knight1, knight2):
    apply_damage(knight2, knight1)
    apply_damage(knight1, knight2)
