def armour_protection(armours: dict) -> int:
    protection = 0
    for armour in armours:
        protection += armour["protection"]
    return protection
