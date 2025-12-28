from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def __str__(self) -> str:
        return f"{self.name}: {self.hp}"

    def __gt__(self, other: Knight) -> bool:
        return self.hp > other.hp

    def __lt__(self, other: Knight) -> bool:
        return self.hp < other.hp

    def __eq__(self, other: Knight) -> bool:
        return self.hp == other.hp

    @staticmethod
    def creation(knights_config: dict) -> list[Knight]:
        list_of_knights = []
        for knight in knights_config.values():
            power = knight["power"] + knight["weapon"]["power"]
            hp = knight["hp"]
            protection = sum(
                [armour["protection"]
                 for armour in knight["armour"]]
            )
            if knight.get("potion"):
                if knight["potion"]["effect"].get("power"):
                    power += knight["potion"]["effect"].get("power")
                if knight["potion"]["effect"].get("hp"):
                    hp += knight["potion"]["effect"].get("hp")
                if knight["potion"]["effect"].get("protection"):
                    protection += knight["potion"]["effect"].get("protection")
            list_of_knights.append(Knight(
                name=knight["name"],
                power=power,
                hp=hp,
                protection=protection
            ))
        return list_of_knights
