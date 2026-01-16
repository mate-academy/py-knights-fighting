from typing import Union


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: Union[dict, None]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.potion = potion
        self.armour = armour
        self.apply_armour(self.armour)
        self.apply_weapon(self.weapon)
        if potion is not None:
            self.apply_potion(self.potion)

#ta funckje wywolac na obiekcie
    def apply_armour(self, armours: list) -> None:
        self.protection = sum(armour["protection"] for armour in armours
                              )

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict):
        for ability, value in potion["effect"].items():
            if hasattr(self, ability):
                setattr(self,ability, getattr(self,ability) + value)

    def display_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"HP: {self.hp}")
        print(f"Protection: {self.protection}")
        print(f"Weapon: {self.weapon['name']} (Power: {self.weapon['power']})")
        print("Armour:")
        for armour in self.armour:
            print(f"  - {armour['part']}: {armour['protection']} protection")
        if self.potion:
            print("Potion effects:")
            for ability, value in self.potion["effect"].items():
                print(f"  - {ability}: +{value}")
        else:
            print("Potion: None")





