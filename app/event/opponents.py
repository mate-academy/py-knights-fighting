from app.event.battle import Battle


def sparring(warriors: list) -> dict:
    first_warrior = "Absent"
    second_warrior = "Absent"
    for man in warriors:
        if man.name == "Lancelot":
            first_warrior = man
        if man.name == "Mordred":
            second_warrior = man
    if first_warrior is not None and second_warrior is not None:
        lancelot_vs_mordred = Battle(first_warrior, second_warrior)
        lancelot_vs_mordred.fight()

    for man in warriors:
        if man.name == "Arthur":
            first_warrior = man
        if man.name == "Red Knight":
            second_warrior = man
    if first_warrior is not None and second_warrior is not None:
        arthur_vs_red_knight = Battle(first_warrior, second_warrior)
        arthur_vs_red_knight.fight()

    result = {}

    for man in warriors:
        result[man.name] = man.hp
    return result
