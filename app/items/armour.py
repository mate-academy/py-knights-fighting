def get_total_protection(armour: list) -> int:
    return sum(piece["protection"] for piece in armour)
