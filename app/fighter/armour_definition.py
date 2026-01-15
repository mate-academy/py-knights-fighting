class Armour:
    @staticmethod
    def count_protection(parts: list) -> int:
        protection = 0
        for part in parts:
            protection += part["protection"]
        return protection
