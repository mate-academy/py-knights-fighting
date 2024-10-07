from app.knights.knights import Knight


class Armour:

    @staticmethod
    def get_armour(knights: Knight, armours: list[dict | None]) -> None:
        for armour in armours:
            knights.protection += armour["protection"]
