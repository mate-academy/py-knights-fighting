from app.knight.knight import Knight


class Power:

    @staticmethod
    def total_power(knight: Knight) -> int:
        total_power = knight.power + knight.weapon["power"]
        if knight.potion is not None and "power" in knight.potion["effect"]:
            total_power += knight.potion["effect"]["power"]
        return total_power
