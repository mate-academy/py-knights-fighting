from app.knight_config.config import Knight


class Potion:
    @staticmethod
    def potions_effect(knight: Knight) -> Knight:
        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]
            if "protection" in knight.potion["effect"]:
                knight.protection += knight.potion["effect"]["protection"]
            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
            return knight
