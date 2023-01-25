from app.preparations.knight_stats import Knight


class Equipment:

    @staticmethod
    def armour_on(knight: Knight, armour: list) -> None:

        for piece_of_equip in armour:
            knight.protection += piece_of_equip["protection"]

    @staticmethod
    def weapons_up(knight: Knight, weapon: dict) -> None:
        knight.power += weapon["power"]

    @staticmethod
    def potion_in(knight: Knight, potion: dict) -> None:

        if "power" in potion:
            knight.power += potion["power"]

        if "protection" in potion:
            knight.protection += potion["protection"]

        if "hp" in potion:
            knight.health += potion["hp"]
