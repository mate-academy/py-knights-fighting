from typing import Any


class Potion:

    @staticmethod
    def apply_potion(potion: dict, knight: Any) -> object:
        if potion is not None:
            if "hp" in potion["effect"]:
                knight.hp += potion["effect"]["hp"]
            if "power" in potion["effect"]:
                knight.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                knight.protection += potion["effect"]["protection"]
        return knight
