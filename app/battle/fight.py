from app.preparations.make_knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> list:
    first_knight_stats = first_knight.prepare_knight()
    second_knight_stats = second_knight.prepare_knight()

    first_knight_hp = (first_knight_stats["hp"]
                       - (second_knight_stats["strength"]
                          - first_knight_stats["protection"]))
    second_knight_hp = (second_knight_stats["hp"]
                        - (first_knight_stats["strength"]
                           - second_knight_stats["protection"]))

    return [max(0, first_knight_hp), max(0, second_knight_hp)]
