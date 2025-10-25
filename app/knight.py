from __future__ import annotations


class Knight:

    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]
        self.power = knight_dict["power"]
        self.hp = knight_dict["hp"]
        self.weapon = knight_dict["weapon"]
        self.armour = knight_dict.get("armour", [])
        self.potion = knight_dict.get("potion", None)
        self.protection = 0

    def prepare_knight(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]
            print(f"{self.name} equip {arm['part']}")

        if self.potion:
            print(f"{self.name} drink {self.potion['name']} potion")
            self.hp += self.potion["effect"].get("hp", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)

        self.power += self.weapon["power"]
        print(f"{self.name} take {self.weapon['name']}")

        print(f"{self.name}: "
              f"power - {self.power}, "
              f" hp - {self.hp}, "
              f" protection - {self.protection}")

    @staticmethod  # just want it in this way :)
    def duel(first: Knight, second: Knight) -> None | str:
        if not (isinstance(first, Knight) and isinstance(second, Knight)):
            return "Only knights can duel"

        if first is second:
            return "You can't duel yourself"

        first.prepare_knight()
        second.prepare_knight()

        first.hp -= second.power - first.protection
        print(f"{second.name} hit {first.name}. "
              f"{first.name} takes {second.power - first.protection} damage!")

        second.hp -= first.power - second.protection
        print(f"{first.name} hit {second.name}. "
              f"{second.name} takes {first.power - second.protection} damage!")

        if second.hp <= 0 and first.hp <= 0:
            first.hp = 0
            second.hp = 0
            print("BOTH FALL")
        elif second.hp <= 0:
            second.hp = 0
            print(f"{second.name} fall!")
        elif first.hp <= 0:
            first.hp = 0
            print(f"{first.name} fall!")
        else:
            print("both on legs")
