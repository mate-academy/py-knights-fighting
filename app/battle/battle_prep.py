def knight_stats_preparation(knight: object) -> None:
    knight.protection = 0
    for armory in knight.armour:
        knight.protection += armory["protection"]
    if not knight.power:
        knight.power = 0
    knight.power += knight.weapon["power"]

    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]

        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]

        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]


if __name__ == "__main__":
    pass
