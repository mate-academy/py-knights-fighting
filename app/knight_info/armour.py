class KnightArmour:
    @staticmethod
    def total_armour(armours: list) -> int:
        protection = 0
        for armour in armours:
            protection += armour["protection"]

        return protection
