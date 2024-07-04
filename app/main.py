from app.config.knights import KNIGHTS
from app.models.knight import Knight
from app.battle import battle


def prepare_knight(knight_config: dict) -> "Knight":
    return Knight(
        name=knight_config["name"],
        power=knight_config["power"],
        hp=knight_config["hp"],
        armour=knight_config["armour"],
        weapon=knight_config["weapon"],
        potion=knight_config["potion"]
    )


def main() -> None:
    lancelot = prepare_knight(KNIGHTS["lancelot"])
    arthur = prepare_knight(KNIGHTS["arthur"])
    mordred = prepare_knight(KNIGHTS["mordred"])
    red_knight = prepare_knight(KNIGHTS["red_knight"])

    battle_result1 = battle(lancelot, mordred)
    battle_result2 = battle(arthur, red_knight)

    print(battle_result1)
    print(battle_result2)


if __name__ == "__main__":
    main()
