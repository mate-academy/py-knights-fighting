class Hero:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: int = 0) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value if value >= 0 else 0

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
                fighter["power"] += potion_effect.get("power", 0)
                fighter["hp"] += potion_effect.get("hp", 0)
                fighter["armour"] += potion_effect.get("protection", 0)

        for knight in dict_of_knights.values():
            for data in knights_data.values():
                if knight.name == data["name"]:
                    knight.armour = data["armour"]
                    knight.power = data["power"]
                    knight.hp = data["hp"]

        return dict_of_knights
