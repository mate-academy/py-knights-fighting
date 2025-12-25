from __future__ import annotations


class Knight:
    CREATED_KNIGHTS = []

    def __init__(self, dict_knight: dict) -> None:
        self.name = dict_knight["name"]
        self.power = dict_knight["power"] + self.prepare_weapon(
            dict_knight
        )
        self.hp = dict_knight["hp"]
        self.protection = self.put_on_armor(dict_knight)
        self.potion_shot(dict_knight)
        Knight.CREATED_KNIGHTS.append(self)

    @staticmethod
    def put_on_armor(dict_knight: dict) -> int:
        protection = 0
        if dict_knight.get("armour"):
            for unit in dict_knight["armour"]:
                protection += unit["protection"]
        return protection

    @staticmethod
    def prepare_weapon(dict_knight: dict) -> int:
        return dict_knight["weapon"]["power"]

    def potion_shot(self, dict_knight: dict) -> None:
        potion = dict_knight.get("potion")
        if potion:
            for effect, value in potion["effect"].items():
                setattr(self, effect, getattr(self, effect) + value)

    def _do_damage(self, other: Knight) -> None:
        final_hp_damage = (
            0
            if self.power < other.protection
            else self.power - other.protection
        )

        if other.hp - final_hp_damage < 0:
            other.hp = 0
        else:
            other.hp -= final_hp_damage

    def exchange_shots(self, other: Knight) -> None:
        self._do_damage(other)
        other._do_damage(self)

    @classmethod
    def show_hp(cls) -> dict:
        return {
            knight.name: knight.hp for knight in cls.CREATED_KNIGHTS
        }
