from app.battle.battle import attack, check_survival
from app.battle.preparation import preparation_for_battle
from app.character.knight import Knight
from app.character.config import KNIGHTS


def battle(knights_data: dict) -> dict:
    arthur = Knight(**knights_data["arthur"])
    lancelot = Knight(**knights_data["lancelot"])
    mordred = Knight(**knights_data["mordred"])
    red_knight = Knight(**knights_data["red_knight"])

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
    knights_data = KNIGHTS

    result = battle(knights_data)

    for knight, hp in result.items():
        print(f"{knight}: {hp}")


if __name__ == "__main__":
    main()
