from .knight import Knight


def battle(knights_config: dict, max_rounds: int | None = 1) -> dict[str, int]:
    battles_table = {
        "round_0": [
            ("lancelot", "mordred"),
            ("arthur", "red_knight")
        ]
    }

    all_knights = {
        knight_name: Knight(**knight_data)
        for knight_name, knight_data in knights_config.items()
    }

    for knight_class in all_knights.values():
        knight_class.prepare_to_fight()

    for round_number in range(max_rounds):
        next_round = []

        if f"round_{round_number}" not in battles_table:
            break

        for (
            first_opponent,
            second_opponent
        ) in battles_table[f"round_{round_number}"]:
            winner = (all_knights[first_opponent]
                      .fight(all_knights[second_opponent]))
            next_round.append(winner)

        if len(next_round) < 2:
            break

        battles_table[f"round_{round_number + 1}"] = [
            (next_round[idx], next_round[idx + 1])
            for idx in range(0, len(next_round), 2)
        ]

    return {
        knight_class.name: knight_class.hp
        for knight_class in all_knights.values()
    }
