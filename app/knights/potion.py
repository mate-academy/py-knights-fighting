from app.knights.knight import Knight


class Potion:
    @staticmethod
    def apply_potion(knight: Knight) -> None:
        if not knight.potion:
            pass
        else:
            if "hp" in knight.potion["effect"]:
                knight.health += knight.potion["effect"]["hp"]
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]
            if "protection" in knight.potion["effect"]:
                knight.armour += knight.potion["effect"]["protection"]

        knight.potion = ["0 Potions"]
