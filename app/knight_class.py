from __future__ import annotations


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data.get("name")
        self.power = self.calc_stat(knight_data, "power")
        self.hp = self.calc_stat(knight_data, "hp")
        self.protection = self.calc_stat(knight_data, "protection")

    def calc_stat(self, kd: dict | list, stat: str) -> int:
        res_stat = 0

        for key, value in kd.items():
            if isinstance(value, dict):
                res_stat += self.calc_stat(value, stat)
            if isinstance(value, list):
                for elem in value:
                    res_stat += self.calc_stat(elem, stat)
            elif key == stat:
                res_stat += value

        return res_stat

    def fight(self, knight_x: Knight) -> None:
        self.hp -= knight_x.power - self.protection
        self.check_def()

    def check_def(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def check_hp(self) -> int:
        return self.hp
