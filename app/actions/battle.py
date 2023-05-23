from app.people.knight import Knight


def attack(knight1: "Knight", knight2: "Knight") -> int:
    if knight2.battle_stats["power"] <= knight1.battle_stats["protection"]:
        return knight1.battle_stats["hp"]
    elif knight1.battle_stats["hp"] \
            - knight2.battle_stats["power"] \
            + knight1.battle_stats["protection"] <= 0:
        return 0
    else:
        return knight1.battle_stats["hp"] \
            - knight2.battle_stats["power"] \
            + knight1.battle_stats["protection"]


# preset battle
def battle(dict_of_knights: dict) -> dict:
    list_of_knight_instances = []
    for knight_key, knight_data in dict_of_knights.items():
        knight = Knight(knight_data["name"],
                        knight_data["power"],
                        knight_data["hp"],
                        knight_data["armour"],
                        knight_data["weapon"],
                        knight_data["potion"])
        list_of_knight_instances.append(knight)
    lancelot = list_of_knight_instances[0]
    arthur = list_of_knight_instances[1]
    mordred = list_of_knight_instances[2]
    red_knight = list_of_knight_instances[3]

    # returns hp of knight1 after hit from knight2

    result_of_battle = {
        lancelot.name: attack(lancelot, mordred),
        arthur.name: attack(arthur, red_knight),
        mordred.name: attack(mordred, lancelot),
        red_knight.name: attack(red_knight, arthur)
    }

    return result_of_battle
