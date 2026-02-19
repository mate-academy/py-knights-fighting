from app.knight import Knight
from app.config import KNIGHTS


def run_duel(attacker: Knight, defender: Knight) -> None:

    damage_to_attacker = attacker.calculate_damage_from(defender)
    damage_to_defender = defender.calculate_damage_from(attacker)

    attacker.take_damage(damage_to_attacker)
    defender.take_damage(damage_to_defender)


def battle(knights_config: dict) -> dict:

    knights = []
    for name, knight in knights_config.items():
        knights.append(Knight(knight))

    run_duel(knights[0], knights[2])
    run_duel(knights[1], knights[3])

    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
