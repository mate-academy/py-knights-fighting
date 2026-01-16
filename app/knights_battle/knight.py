from __future__ import annotations


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int,
            knight: dict
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.knight = knight
        self.apply_armour(knight)
        self.apply_weapon(knight)
        self.apply_potion(knight)

    def apply_armour(self, knight: dict) -> None:
        self.protection += sum(el["protection"] for el in knight["armour"])

    def apply_weapon(self, knight: dict) -> None:
        self.power += knight["weapon"]["power"]

    def apply_potion(self, knight: dict) -> None:
        if knight["potion"] is not None:
            for value in knight["potion"]["effect"]:
                if value == "power":
                    setattr(
                        self,
                        "power",
                        knight["potion"]["effect"][value] + self.power
                    )

                if value == "hp":
                    setattr(
                        self,
                        "hp",
                        knight["potion"]["effect"][value] + self.hp
                    )

                if value == "protection":
                    setattr(
                        self,
                        "protection",
                        knight["potion"]["effect"][value] + self.protection
                    )

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection

    def check_if_someone_fell_in_battle(self) -> None:
        self.hp = max(0, self.hp)
