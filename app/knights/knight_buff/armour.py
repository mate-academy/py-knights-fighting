class Armour:
    """
    method for armour donning, armour = KNIGHTS[name]["armour"]
    """
    @staticmethod
    def all_armour(armour, knight):

        for part in armour:
            knight.protection += part["protection"]
        return knight
