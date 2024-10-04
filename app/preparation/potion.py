from typing import List

from app.knights.knights import Knight


class Potion:

    @staticmethod
    def get_potion(knights: List[Knight], potion: dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                knights.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                knights.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                knights.hp += potion["effect"]["hp"]
