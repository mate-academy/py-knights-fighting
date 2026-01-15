class Protection:

    @staticmethod
    def knight_protection(knight_armour: list,
                          protection: int,
                          effect_protection: int
                          ) -> int:
        if knight_armour is []:
            protection = 0
        else:
            for ar in knight_armour:
                protection += ar["protection"]
            protection += effect_protection
        return protection
