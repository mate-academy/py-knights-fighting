class Power:

    @staticmethod
    def knight_power(power: int, weapon_power: int, effect_power: int) -> int:
        power += weapon_power + effect_power
        return power
