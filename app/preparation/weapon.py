from app.knights.knights import Knight


class Weapon:

    @staticmethod
    def get_weapon(knights: Knight, weapon: dict) -> None:
        knights.power += weapon["power"]
