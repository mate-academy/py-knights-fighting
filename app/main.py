from app.knights_data import KNIGHTS
from app.battle_preparations import preparing_knight_to_battle
from app.battles import final_battle


def battle(knights_config: dict) -> dict:
    set_pairs_of_warriors = [["Lancelot", "Mordred"], ["Arthur", "Red Knight"]]

    for knight_person in knights_config.values():
        preparing_knight_to_battle(knight_person)

    return final_battle(set_pairs_of_warriors)


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
