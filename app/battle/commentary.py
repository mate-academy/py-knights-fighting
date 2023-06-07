from __future__ import annotations
from app.battle.preparation import Knights


class Commentary:
    battle_counter = 0
    battle_list = ["first", "second"]
    power_stats = []

    def __init__(self, knight: Knights) -> None:
        self.name = knight.name
        self.power = knight.power
        self.power_stats.append(self.power)

    @staticmethod
    def opening_com() -> None:
        print("Welcome! At UKC 2023 half-finals!\n"
              "And welcome our contenders for The Title of "
              "Ultimate Knight Champion!")

    @staticmethod
    def before_battle_com() -> None:
        print("\nContenders are ready! Make your final bets "
              "because the battles start now!")

    @staticmethod
    def end_com() -> None:
        print("\nSee you soon at UKC 2023 finals!\n"
              "Here are the results of today's brave fighting:")

    @classmethod
    def battle_com(cls, knight1: Knights, knight2: Knights) -> None:
        print(f"\nIn {Commentary.battle_list[Commentary.battle_counter]} "
              f"battle we have {knight1.name} vs {knight2.name}")

        if knight1.hp == 0:
            print(f"{knight2.name} lands a fatal blow on {knight1.name} "
                  f"with his handy {knight2.weapon_name}")
            print("But before dying, on his final breath...")
        else:
            print(f"{knight2.name} strikes {knight1.name} "
                  f"with his handy {knight2.weapon_name}")

        if knight2.hp == 0:
            print(f"{knight1.name} strikes back with a killing blow on "
                  f"{knight2.name} with his mighty {knight1.weapon_name}")
        else:
            print(f"{knight1.name} strikes back {knight2.name} "
                  f"with his mighty {knight1.weapon_name}")

        if knight1.hp == 0:
            print(f"R.I.P. {knight1.name}.\n"
                  f"Congratulate the winner {knight2.name}!")
        elif knight2.hp == 0:
            print(f"R.I.P {knight2.name}.\n"
                  f"Congratulate the winner {knight1.name}!")
        else:
            print("Friendship won!")
        Commentary.battle_counter += 1
        if Commentary.battle_counter == 2:
            Commentary.battle_counter = 0

    @staticmethod
    def introduction(knight: Commentary) -> None:
        print(f"\n{knight.name}!")
        if knight.power == min(Commentary.power_stats):
            print("*crowd booing*")
        elif knight.power == max(Commentary.power_stats):
            print("*crowd goes wild*")
        else:
            print("*crowd is cheering*")
