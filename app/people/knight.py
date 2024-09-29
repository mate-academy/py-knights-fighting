from app.people.person import Person


class Knight(Person):

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict) -> None:
        super().__init__(name, power, hp)
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def battle(knights_dict: dict) -> dict:
        knights_res = {}
        for knight_name, knight_stats in knights_dict.items():
            knights_res[knight_name] = (Knight(knight_stats.get("name"),
                                               knight_stats.get("power"),
                                               knight_stats.get("hp"),
                                               knight_stats.get("armour"),
                                               knight_stats.get("weapon"),
                                               knight_stats.get("potion")))
        return knights_res
