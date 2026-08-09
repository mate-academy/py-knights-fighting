def create_armour(part: str, protection: int) -> dict:
    return {"part": part, "protection": protection}


def get_total_protection(armour_list: list) -> int:
    return sum(item["protection"] for item in armour_list)
