def armour_protection(armours: dict) -> int:
    protection = 0
    for i in armours:
        protection += i["protection"]
    return protection
