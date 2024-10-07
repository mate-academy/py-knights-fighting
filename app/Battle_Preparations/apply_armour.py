def apply_armour(knights_attr: dict):
    for stats in knights_attr.values():
        for armour in stats.armour:
            stats.protection += armour["protection"]
