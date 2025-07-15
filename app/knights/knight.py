from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(
            self,
            knight_dict: dict[str, str | int | list | dict]
    ) -> None:
        self.name: str = knight_dict.get("name")
        self.power: int = knight_dict.get("power")
        self.hp: int = knight_dict.get("hp")

        self.protection: int = 0

        self.armour: list[Armour] = self.__init_armour(
            knight_dict.get("armour")
        )
        self.weapon: Weapon = self.__init_weapon(
            knight_dict.get("weapon")
        )
        self.potion: Potion | None = self.__init_potion(
            knight_dict.get("potion")
        )

    def prepare_to_battle(self) -> None:
        for armour_piece in self.armour:
            self.protection += armour_piece.protection

        self.power += self.weapon.power

        if self.potion is not None:
            for stat in ["power", "protection", "hp"]:
                if stat in self.potion.effect:
                    self[stat] += self.potion.effect[stat]

    def __init_armour(
            self,
            armour_list: list[dict[str, str | int]]
    ) -> list[Armour]:
        return [
            Armour(armour_dict=armour_dict)
            for armour_dict in armour_list
        ]

    def __init_weapon(self, weapon_dict: dict[str, str | int]) -> Weapon:
        return Weapon(weapon_dict)

    def __init_potion(
            self,
            potion_dict: dict[
                str,
                str | dict[str, int]
            ] | None
    ) -> Potion | None:
        if potion_dict is None:
            return None

        return Potion(potion_dict)

    def __getitem__(self, item: object) -> str | int | None:
        if item == "power":
            return self.power

        if item == "protection":
            return self.protection

        if item == "hp":
            return self.hp

        return None

    def __setitem__(self, key: str, value: str | int) -> None:
        if key == "power":
            self.power = value

        if key == "protection":
            self.protection = value

        if key == "hp":
            self.hp = value
