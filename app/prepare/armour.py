def armour(arm: list) -> int:
    protection = 0
    for each in arm:
        protection += each["protection"]
    return protection
