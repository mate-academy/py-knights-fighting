from app.battle.battle import attack, check_survival
from app.battle.preparation import preparation_for_battle
from app.character.knights import Knights


def battle(knights_data: dict) -> dict:
    arthur = Knights(**knights_data["arthur"])
    lancelot = Knights(**knights_data["lancelot"])
    mordred = Knights(**knights_data["mordred"])
    red_knight = Knights(**knights_data["red_knight"])

    prepared_arthur = preparation_for_battle(arthur)
    prepared_lancelot = preparation_for_battle(lancelot)
    prepared_mordred = preparation_for_battle(mordred)
    prepared_red_knight = preparation_for_battle(red_knight)

    attack(prepared_lancelot, prepared_mordred)

    check_survival(prepared_lancelot)
    check_survival(prepared_mordred)

    attack(prepared_arthur, prepared_red_knight)

    check_survival(prepared_arthur)
    check_survival(prepared_red_knight)

    return {
        prepared_lancelot.name: prepared_lancelot.hp,
        prepared_mordred.name: prepared_mordred.hp,
        prepared_arthur.name: prepared_arthur.hp,
        prepared_red_knight.name: prepared_red_knight.hp,
    }


def main() -> None:
    knights_data = {
        "arthur": {...},
        "lancelot": {...},
        "mordred": {...},
        "red_knight": {...},
    }

    result = battle(knights_data)

    for knight, hp in result.items():
        print(f"{knight}: {hp}")


if __name__ == "__main__":
    main()
