from app.knights import Knight


class Arena:
    @staticmethod
    def opposition(knights: dict) -> dict:
        dict_knights = {}
        for key, value in knights.items():
            knight = Knight(value["name"], value["power"],
                            value["hp"])
            knight.use_weapon(value["weapon"]["power"])
            if value["armour"] is not None:
                knight.use_armour(value["armour"])
            if value["potion"] is not None:
                knight.use_potion(value["potion"]["effect"])
            dict_knights[key] = knight

        dict_knights["lancelot"].hp -= dict_knights["mordred"].power
        dict_knights["mordred"].hp -= dict_knights["lancelot"].power
        dict_knights["arthur"].hp -= dict_knights["red_knight"].power
        dict_knights["red_knight"].hp -= dict_knights["arthur"].power
        return dict_knights
