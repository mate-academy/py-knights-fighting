from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_knight_statistics(self) -> dict:
        hp = self.hp
        power = self.power + self.weapon["power"]
        protection = 0

        for armour_type in self.armour:
            protection += armour_type["protection"]

        if self.potion is not None:
            effect = self.potion.get("effect")
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)
            hp += effect.get("hp", 0)

        return {
            "hp": hp,
            "power": power,
            "protection": protection
        }


class Battle:
    def __init__(self, first_fighter: Knight, second_fighter: Knight) -> None:
        self.first_fighter = first_fighter
        self.second_fighter = second_fighter

    @staticmethod
    def normalize_hp(hp: int) -> int:
        if hp < 0:
            return 0

        return hp

    def battle(self) -> dict:
        f_fighter = self.first_fighter.get_knight_statistics()
        s_fighter = self.second_fighter.get_knight_statistics()

        first_fighter_hp = (
            f_fighter["hp"] + f_fighter["protection"] - s_fighter["power"]
        )
        second_fighter_hp = (
            s_fighter["hp"] + s_fighter["protection"] - f_fighter["power"]
        )

        return {
            self.first_fighter.name: self.normalize_hp(first_fighter_hp),
            self.second_fighter.name: self.normalize_hp(second_fighter_hp),
        }


class Championship:
    def __init__(self, knights: dict, battle_pairs: dict) -> None:
        self.knights = knights
        self.battle_pairs = battle_pairs
        self.battles_instance = []

    def preparation_championship(self) -> None:

        for first_name, second_name in self.battle_pairs.values():
            first_param = self.knights.get(first_name)
            second_param = self.knights.get(second_name)

            battle = Battle(
                first_fighter=Knight(**first_param),
                second_fighter=Knight(**second_param)
            )
            self.battles_instance.append(battle)

    def start_championship(self) -> None:
        for battle in self.battles_instance:
            battle.battle()

    def result_championship(self) -> dict:
        result = {}

        for battle in self.battles_instance:
            result.update(battle.battle())

        return result
