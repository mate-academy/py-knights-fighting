from __future__ import annotations
from app.comment_generator.commentator import (
    comment_on_preparation,
    comment_of_end_duel,
    advertising,
    the_results_of_the_match
)


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 set_of_armor: list,
                 weapon: dict,
                 potion: dict | None
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = Knight.armor(set_of_armor)
        self.weapon = weapon["power"]
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> Knight:
        self.protection += self.armor
        self.power += self.weapon
        if self.potion:
            effect = self.potion["effect"]
            for specialty, boost in effect.items():
                if specialty == "hp":
                    self.hp += effect["hp"]
                elif specialty == "power":
                    self.power += effect["power"]
                elif specialty == "protection":
                    self.protection += effect["protection"]
        print(comment_on_preparation(self.name))
        print(advertising())
        return self

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
        winner_loser = sorted([other, self], key=lambda x: x.hp, reverse=True)
        winner, loser = winner_loser[0].name, winner_loser[1].name
        print(comment_of_end_duel(winner=winner, loser=loser))
        print(advertising())

    @classmethod
    def final_result(cls, knights_dict: dict) -> None:
        knights_list = [knight for knight in knights_dict.values()]
        knights_list.sort(key=lambda x: x.hp, reverse=True)
        final_message = the_results_of_the_match(
            first_place=knights_list[0].name,
            second_place=knights_list[1].name,
            third_place=knights_list[2].name,
            fourth_place=knights_list[3].name
        )
        print(final_message)

    @classmethod
    def armor(cls, set_of_armor: list) -> int:
        if set_of_armor:
            return sum(
                [armor_part["protection"]
                 for armor_part in set_of_armor]
            )
        return 0

    @classmethod
    def create_knight_from_dict(cls, dict_of_knights: dict) -> Knight:
        return cls(
            name=dict_of_knights["name"],
            power=dict_of_knights["power"],
            hp=dict_of_knights["hp"],
            set_of_armor=dict_of_knights["armour"],
            weapon=dict_of_knights["weapon"],
            potion=dict_of_knights["potion"]
        )
