from __future__ import annotations


class Knight:

    # list of knights [mnemonic_name : knight_obj]
    knights = {}

    def __init__(self, knight: str, name: str, power: int, hp: int) -> None:
        # main parameters
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        # additional features
        self.armour = []
        self.weapon = {}
        self.potion = None
        # add to list of knights
        Knight.knights[knight] = self

    def add_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.armour.append({"part": armour["part"],
                                "protection": armour["protection"]})

    def add_weapon(self, weapon_dict: dict) -> None:
        self.weapon = {"name": weapon_dict["name"],
                       "power": weapon_dict["power"]}

    def add_potion(self, potion_dict: dict = None) -> None:
        if potion_dict is None:
            return
        self.potion = {"name": potion_dict["name"],
                       "effect": {key: val for (key, val)
                                  in potion_dict["effect"].items()}}

    def __repr__(self) -> str:
        return f""" {self.name} | power: {self.power} hp: {self.hp} protection: {self.protection}
        armour= {self.armour}
        weapon= {self.weapon}
        potion= {self.potion}"""

    def prepare(self) -> None:
        # apply additional features for knight

        # apply armour
        for arm in self.armour:
            self.protection += arm["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def fight(self, other: Knight) -> None:
        # self. vs other.

        # prepare both knights before battle
        self.prepare()
        other.prepare()

        # calculate hp after battle
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0

    @classmethod
    def knights_load(cls, knights_config: dict = None) -> None:
        # load knight's from knights_config

        if knights_config is None:
            return

        for knight, unit in knights_config.items():
            # main parameters
            kobj = cls(knight, unit["name"], unit["power"], unit["hp"])
            # additional features
            kobj.add_armour(unit["armour"])
            kobj.add_weapon(unit["weapon"])
            kobj.add_potion(unit["potion"])

    @classmethod
    def battle_result(cls) -> str:
        # Return battle results:
        return {knight.name: knight.hp for knight in Knight.knights.values()}
