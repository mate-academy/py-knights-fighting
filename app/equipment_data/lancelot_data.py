class LancelotData:
    ARMOR_LIST = []
    WEAPON = dict(name="Metal Sword", power=50)


    @staticmethod
    def set_data(armor_list: list, weapon: dict):
        LancelotData.ARMOR_LIST = armor_list
        LancelotData.WEAPON = weapon
