from typing import Any


class Armour:
    @staticmethod
    def all_armour(armour: list, knight: Any) -> object:

        for part in armour:
            knight.protection += part["protection"]
        return knight
