from __future__ import annotations


class Knight:
    whole_knights = {}

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 prot_game: int,
                 power_game: int,
                 hp_game: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.prot_game = prot_game
        self.power_game = power_game
        self.hp_game = hp_game

    @staticmethod
    def protection_for_game(knights_list: dict) -> int:
        prot_game = 0
        for elem in knights_list["armour"]:
            prot_game += elem["protection"]
        if (knights_list["potion"] is not None
                and "protection" in knights_list["potion"]["effect"]):
            prot_game += knights_list["potion"]["effect"]["protection"]
        return prot_game

    @staticmethod
    def power_for_game(knights_list: dict) -> int:
        power_game = knights_list["power"] + knights_list["weapon"]["power"]
        if (knights_list["potion"] is not None
                and "power" in knights_list["potion"]["effect"]):
            power_game += knights_list["potion"]["effect"]["power"]
        return power_game

    @staticmethod
    def hp_for_game(knights_list: dict) -> int:
        hpgame = knights_list["hp"]
        if (knights_list["potion"] is not None
                and "hp" in knights_list["potion"]["effect"]):
            hpgame += knights_list["potion"]["effect"]["hp"]
        return hpgame

    @classmethod
    def init_knights(cls, key_name: str, knights_list: dict) -> Knight:

        inst_ce = Knight(knights_list["name"],
                         knights_list["power"],
                         knights_list["hp"],
                         Knight.protection_for_game(knights_list),
                         Knight.power_for_game(knights_list),
                         Knight.hp_for_game(knights_list))
        cls.whole_knights[key_name] = inst_ce
        return inst_ce

    @classmethod
    def battle_two_knights(cls, knight_1: str, knight_2: str) -> None:
        kni_1 = cls.whole_knights[knight_1]
        kni_2 = cls.whole_knights[knight_2]
        kni_1.hp_game -= kni_2.power_game - kni_1.prot_game
        kni_2.hp_game -= kni_1.power_game - kni_2.prot_game

        if kni_1.hp_game <= 0:
            kni_1.hp_game = 0

        if kni_2.hp_game <= 0:
            kni_2.hp_game = 0

    @classmethod
    def return_result(cls) -> dict:
        return {value.name:
                value.hp_game
                for key, value in cls.whole_knights.items()}
