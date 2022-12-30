from typing import Union


class Knights:

    all_created_knights = {}

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: Union[dict, None],
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = (
            sum([i["protection"] if "protection" in i.keys()
                 else 0 for i in armour])
            if self.armour
            else 0
        )
        if self.weapon:
            self.power += self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"].keys():
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"].keys():
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"].keys():
                self.hp += self.potion["effect"]["hp"]
        self.all_created_knights[self.name] = self
