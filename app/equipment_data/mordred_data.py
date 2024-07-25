class MordredData:
    ARMOR_LIST = [
        {"part": "breastplate", "protection": 15},
        {"part": "boots", "protection": 10}
    ]
    WEAPON = dict(name="Poisoned Sword", power=60)

    @staticmethod
    def set_data(armor_list: list, weapon: dict):
        MordredData.ARMOR_LIST = armor_list
        MordredData.WEAPON = weapon
