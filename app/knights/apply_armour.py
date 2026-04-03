class Armour:

    @staticmethod
    def app_armour(armour: dict):
        protection = 0
        for part in armour:
            protection += part["protection"]
        return protection
