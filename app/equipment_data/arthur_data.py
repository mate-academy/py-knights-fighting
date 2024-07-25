class ArthurData:
    ARMOR_LIST = [
        {
            "part": "helmet",
            "protection": 15,
        },
        {
            "part": "breastplate",
            "protection": 20,
        },
        {
            "part": "boots",
            "protection": 10,
        }
    ]
    WEAPON = dict(name="Two-handed Sword", power=55)

    @staticmethod
    def set_data(armor_list: list, weapon: dict):
        ArthurData.ARMOR_LIST = armor_list
        ArthurData.WEAPON = weapon
