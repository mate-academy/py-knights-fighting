from app.knights_info.characters_list import create_char


def battle(knight_dict):
    knights = create_char(knight_dict)

    return sparring(knights["lancelot"], knights["mordred"]) | \
        sparring(knights["arthur"], knights["red_knight"])


def sparring(knight1, knight2):
    result1 = knight1.hp - (knight2.power - knight1.protection)
    result2 = knight2.hp - (knight1.power - knight2.protection)
    return {knight1.name: (result1 if result1 > 0 else 0),
            knight2.name: (result2 if result2 > 0 else 0)}
