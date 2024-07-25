class RedKnightData:
    ARMOR_LIST = [
        {
            "part": "breastplate",
            "protection": 25
        }
    ]
    WEAPON = dict(name="Poisoned Sword", power=60)
    @staticmethod
    def set_data(armor_list: list, weapon: dict):
        RedKnightData.ARMOR_LIST = armor_list
        RedKnightData.WEAPON = weapon
