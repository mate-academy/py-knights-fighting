class Weapon:
    """
    method for weapon, weapon = KNIGHTS[name]["weapon"]
    """
    @staticmethod
    def add_weapon(weapon, knight):
        knight.power += weapon["power"]
        return knight
