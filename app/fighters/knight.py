class Knight:
    dict_of_all_knights_instances = {}

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: dict,
    ) -> object:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.dict_of_all_knights_instances[self.name] = self

    @staticmethod
    def create_dict_of_knights_instances(knights: dict) -> dict:
        dict_of_knights_instances = {}
        for knight in knights.values():
            new_knight = Knight(
                knight["name"],
                knight["power"],
                knight["hp"],
                knight["armour"],
                knight["weapon"],
                knight["potion"],
            )
            dict_of_knights_instances[knight["name"]] = new_knight
        return dict_of_knights_instances
