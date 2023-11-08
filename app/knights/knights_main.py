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

    @classmethod
    def init_knights(cls, key_name: str, knights_list: dict) -> Knight:
        prot_game = 0
        for elem in knights_list["armour"]:
            prot_game += elem["protection"]

        power_game = knights_list["power"] + knights_list["weapon"]["power"]

        hpgame = knights_list["hp"]

        if knights_list["potion"] is not None:
            if "power" in knights_list["potion"]["effect"]:
                power_game += knights_list["potion"]["effect"]["power"]

            if "protection" in knights_list["potion"]["effect"]:
                prot_game += knights_list["potion"]["effect"]["protection"]

            if "hp" in knights_list["potion"]["effect"]:
                hpgame += knights_list["potion"]["effect"]["hp"]

        inst_ce = Knight(knights_list["name"],
                         knights_list["power"],
                         knights_list["hp"],
                         prot_game,
                         power_game,
                         hpgame)
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
        return {cls.whole_knights[key].name:
                cls.whole_knights[key].hp_game
                for key in cls.whole_knights}
