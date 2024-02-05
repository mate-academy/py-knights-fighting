from app.knights.knight import Knight
from app.knights.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(config) for name, config in knights_config.items()}

    def fight(knight1: Knight, knight2: Knight) -> None:
        damage_to_knight2 = max(0, knight1.power - knight2.protection)
        damage_to_knight1 = max(0, knight2.power - knight1.protection)

        knight1.hp -= damage_to_knight1
        knight2.hp -= damage_to_knight2

        knight1.hp = max(0, knight1.hp)
        knight2.hp = max(0, knight2.hp)

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knights[name].name: knights[name].hp
        for name in ["lancelot", "arthur", "mordred", "red_knight"]
    }


def main() -> None:
    battle_results = battle(KNIGHTS)
    print("Battle outcomes:", battle_results)


if __name__ == "__main__":
    main()
