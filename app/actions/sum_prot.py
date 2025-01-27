def sum_protection(armours: list[dict]) -> int:
    final_protection = 0
    for armour in armours:
        final_protection += armour["protection"]
    return final_protection
