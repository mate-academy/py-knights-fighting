class Armour:

    @staticmethod
    def app_armour(armour: dict):
        protection = 0
        for a in armour:
            protection += a["protection"]
        return protection
