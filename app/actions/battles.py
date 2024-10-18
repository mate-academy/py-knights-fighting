def duel(knight1: dict, knight2: dict) -> dict:
    knight1["hp"] -= (knight2["power"] - knight1["add_some_abilities"])
    knight2["hp"] -= (knight1["power"] - knight2["add_some_abilities"])


def check_fell(hp: int) -> bool:
    if hp < 0:
        return True
