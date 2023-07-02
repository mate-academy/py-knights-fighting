from __future__ import annotations

from app.knights.knights_bases import KNIGHTS
from app.support_functions.get_class_attrs \
    import get_class_attribute as gca


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict] | None,
                 weapon: dict | None,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour_info = armour
        self.weapon_info = weapon
        self.potion_info = potion
        self.__preparation_for_battle__()

    def __preparation_for_battle__(self) -> None:
        power, protection, hp = "power", "protection", "hp"
        for armour in self.armour_info:
            self.protection += armour[protection]
        self.power += self.weapon_info[power]
        if self.potion_info:
            attrs_dict = {power: self.power,
                          protection: self.protection, hp: self.hp}
            for attr_name, value in attrs_dict.items():
                setattr(self, attr_name,
                        self.__set_potion_effect__(attr_name, value))

    def __set_potion_effect__(self, needed_param: str, value: int) -> int:
        effect = "effect"
        if needed_param in self.potion_info[effect] \
                and type(self.potion_info[effect][needed_param]
                         ) == type(value):
            value += self.potion_info[effect][needed_param]
        return value

    @staticmethod
    def create_knight(knights: dict[dict]) -> list[Knight]:
        """This method creates list of Knights objects.
        Method uses only corrected knights data."""
        knights_objs = []
        knight_attrs = gca(Knight)
        for battle_params in knights.values():
            init_attrs = knight_attrs.copy()
            for param, value in battle_params.items():
                if param in knight_attrs:
                    init_attrs[param] = value
            knights_objs.append(Knight(*tuple(init_attrs.values())))
        return knights_objs


if __name__ == '__main__':
    knights = Knight.create_knight(KNIGHTS)
    for knight in knights:
        print(knight.name, [knight.hp,
                            knight.power,
                            knight.protection]
              )
