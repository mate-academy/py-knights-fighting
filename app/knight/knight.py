from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict
                 ) -> None:
        self.__name = name
        self.__power = power
        self.__protection = 0
        self.__hp = hp
        self.__armour = armour
        self.__weapon = weapon
        self.__potion = potion

    def prepare_to_battle(self) -> None:
        self.__apply_armour()
        self.__apply_weapon()

        if self.__potion is not None:
            self.__apply_potion()

    def __apply_armour(self) -> None:
        self.__protection = sum(item["protection"] for item in self.__armour)

    def __apply_weapon(self) -> None:
        self.__power += self.__weapon["power"]

    def __apply_potion(self) -> None:
        potion_effect = self.__potion["effect"]

        if "power" in potion_effect:
            self.__power += potion_effect["power"]

        if "protection" in potion_effect:
            self.__protection += potion_effect["protection"]

        if "hp" in potion_effect:
            self.__hp += potion_effect["hp"]

    @property
    def name(self) -> str:
        return self.__name

    @property
    def hp(self) -> int:
        return self.__hp

    def __sub__(self, other: Knight) -> None:
        self.__hp -= other.__power - self.__protection
        self.__reset_hp()

    def __reset_hp(self) -> None:

        if self.__hp <= 0:
            self.__hp = 0
