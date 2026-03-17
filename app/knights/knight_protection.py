def get_protection(armour: list) -> int:
    protection = 0
    if len(armour) == 0:
        return protection
    for part in armour:
        protection += part["protection"]
    return protection
