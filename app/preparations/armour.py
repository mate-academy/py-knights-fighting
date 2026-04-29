def apply_armour(knight: object) -> None:
    for armour in knight.armour:
        knight.protection += armour["protection"]
