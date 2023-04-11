from typing import List

from app.knight import Knight


def update_knights_list(knights_list: List[Knight]) -> None:
    for our_knight in knights_list:
        if our_knight.armour:
            for armor in our_knight.armour:
                our_knight.protection += armor["protection"]

        our_knight.power += our_knight.weapon["power"]

        if our_knight.potion:
            if "power" in our_knight.potion["effect"].keys():
                our_knight.power += our_knight.potion["effect"]["power"]

            if "hp" in our_knight.potion["effect"].keys():
                our_knight.hp += our_knight.potion["effect"]["hp"]

            if "protection" in our_knight.potion["effect"].keys():
                our_knight.protection += \
                    our_knight.potion["effect"]["protection"]
