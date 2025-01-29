# from app.knights.preparations import Knight
# from app.knights.information import KNIGHTS

from app.event.battle import Battle

# from knights.preparations import Knight
# from knights.information import KNIGHTS

def sparring(wariers):
    first_warior = None
    second_warior = None
    for man in wariers:
        if man.name == "Lancelot":
            first_warior = man
        if man.name == "Mordred":
            second_warior = man
    lancelot_vs_mordred = Battle(first_warior, second_warior)
    lancelot_vs_mordred.fight()

    for man in wariers:
        if man.name == "Arthur":
            first_warior = man
        if man.name == "Red Knight":
            second_warior = man
    arthur_vs_red_knight = Battle(first_warior, second_warior)
    arthur_vs_red_knight.fight()

    result = {}

    for man in wariers:
        result[man.name] = man.hp
    return result
