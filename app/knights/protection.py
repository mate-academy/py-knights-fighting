from app.knights.knight import Knight


class Protection:
    @staticmethod
    def apply_protection(knight: Knight) -> None:
        if not knight.armour:
            pass
        protection = 0
        for item in knight.armour:
            protection += item["protection"]
        knight.armour = protection
