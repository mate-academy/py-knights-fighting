from app.fighters.knight import Knight
from app.battle.fight import Fight


def battle(base_knights_config: dict) -> dict:
    fighters = Knight.create_dict_of_knights_instances(base_knights_config)
    lancelot, arthur, mordred, red_knight = fighters.values()

    print("FIRST FIGHT - Lancelot VS Mordred\n")
    Fight.fight(lancelot, mordred)

    print("SECOND FIGHT - Arthur VS Red Knight\n")
    Fight.fight(arthur, red_knight)

    return {
        "Lancelot": lancelot.hp,
        "Arthur": arthur.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp,
    }
