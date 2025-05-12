def calculate_protection(knight: list, knight_protection: dict) -> int:
    protection = sum([i["protection"] for i in knight])
    if knight_protection is not None and "protection" in knight_protection["effect"]:
        protection += knight_protection["effect"]["protection"]
    return protection