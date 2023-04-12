from typing import List

from app.knight import Knight


def calculate_knights_stats(knights_list: List[Knight]) -> None:
    for our_knight in knights_list:
        if our_knight.armour is not None:
            for armor in our_knight.armour:
                our_knight.protection += armor["protection"]

        our_knight.power += our_knight.weapon["power"]

        if our_knight.potion is not None:
            our_knight.power += our_knight.potion["effect"].get("power", 0)
            our_knight.hp += our_knight.potion["effect"].get("hp", 0)
            our_knight.protection += \
                our_knight.potion["effect"].get("protection", 0)
