from app.knight.knight import Knight


class HP:

    @staticmethod
    def total_hp_before_battle(knight: Knight) -> int:

        total_hp_before_battle = knight.hp

        if knight.potion is not None:
            if "hp" in knight.potion["effect"]:
                total_hp_before_battle += knight.potion["effect"]["hp"]
            if "protection" in knight.potion["effect"]:
                total_hp_before_battle += knight.potion["effect"]["protection"]

        for armour_element in knight.armour:
            if "protection" in armour_element:
                total_hp_before_battle += armour_element["protection"]

        return total_hp_before_battle
