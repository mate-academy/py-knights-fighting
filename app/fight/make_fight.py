def get_fight_result(pairs: list, table: dict) -> dict:
    for pair in pairs:
        op1, op2 = pair
        table[op1.display_name] = op1.correct_damage(op2)
        table[op2.display_name] = op2.correct_damage(op1)

    return table
