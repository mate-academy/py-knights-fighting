class Hero:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: int = 0) -> None:

        self.name = name
        self.power = power
        self._hp = hp
        self.armour = armour

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value if value >= 0 else 0

    @staticmethod
    def knights_to_dict(knight_data: dict) -> dict:
        return {data["name"]: Hero(
            data["name"], data["power"], data["hp"]
        ) for data in knight_data.values()
        }

    @staticmethod
    def prepare_knights(
            dict_of_knights: dict,
            knights_data: dict
    ) -> dict:

        for fighter in knights_data.values():
            fighter["armour"] = sum(
                part["protection"] for part in fighter["armour"]
            )
            fighter["power"] += fighter["weapon"]["power"]

            if fighter["potion"]:
                potion_effect = fighter["potion"]["effect"]

                for effect_type, effect_bonus in potion_effect.items():
                    if effect_type == "power":
                        fighter["power"] += effect_bonus
                    elif effect_type == "hp":
                        fighter["hp"] += effect_bonus
                    elif effect_type == "protection":
                        fighter["armour"] += effect_bonus

        for knight in dict_of_knights.values():
            for data in knights_data.values():
                if knight.name == data["name"]:
                    knight.armour = data["armour"]
                    knight.power = data["power"]
                    knight.hp = data["hp"]

        return dict_of_knights
