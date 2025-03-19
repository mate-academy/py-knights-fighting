from __future__ import annotations


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | None,
            weapon: dict,
            potion: dict | None
    ) -> None:
        (
            self.name,
            self.power,
            self.hp,
            self.armour,
            self.weapon,
            self.potion,
            self.protection
        ) = (name, power, hp, armour, weapon, potion, 0)

    def equip_weapon(self) -> None:
        self.power += self.weapon["power"]

    def equip_armour(self) -> None:
        if len(self.armour):
            for piece in self.armour:
                self.protection += piece["protection"]
        else:
            print(f"{self.name} got no armour!")

    def drink_potion(self) -> None:
        if self.potion:
            for stat, effect in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat, 0) + effect)
        else:
            print(f"{self.name} Note: brew a potion for next fights")

    def prepare_to_fight(self) -> None:
        self.equip_weapon()
        self.equip_armour()
        self.drink_potion()

        print(f"{self.name} prepared to fight")

    def fight(self, opponent: Knight) -> Knight | None:
        damage_per_round_self = self.power - opponent.protection
        damage_per_round_opponent = opponent.power - self.protection

        while True:
            if (
                    self.hp <= 0
                    or opponent.hp <= 0
                    or (
                    opponent.hp < damage_per_round_self
                    and self.hp < damage_per_round_opponent
                    )
            ):
                break

            self.hp = max(0, self.hp - damage_per_round_opponent)
            opponent.hp = max(0, opponent.hp - damage_per_round_self)

        if self.hp > opponent.hp:
            return self
        elif self.hp < opponent.hp:
            return opponent
        else:
            return None
