from __future__ import annotations


class KnightPrep:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | None,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon.get("power")
        self.weapon_name = weapon.get("name")
        self.protection = 0
        self.potion = potion

    def apply_weapon(self) -> KnightPrep:
        self.power += self.weapon
        return self

    def apply_armour(self) -> KnightPrep:
        self.protection += sum([part.get("protection")
                                for part in self.armour])
        return self

    def apply_potion(self) -> KnightPrep:
        if self.potion:
            for effect, effect_stats in self.potion["effect"].items():
                self.__dict__[effect] += effect_stats
        return self

    @staticmethod
    def get_ready_for_battle(knight_unprepared: KnightPrep) -> None:
        knight_unprepared.apply_weapon().apply_armour().apply_potion()
