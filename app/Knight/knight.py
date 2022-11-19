from __future__ import annotations


class Knight:
    def __init__(self, knight_key: dict) -> None:
        self.data = knight_key
        self.name = self.data["name"]
        self.hp = self.data["hp"]
        self.power = self.data["power"]
        self.protection = 0
        self.powerup()
        self.armour()
        self.buff()

    def __str__(self) -> str:
        return f"{self.name}: {self.hp}"

    def __repr__(self) -> str:
        return f"{self.name}: {self.hp}"

    def powerup(self) -> None:
        self.power += self.data["weapon"]["power"]

    def armour(self) -> None:
        if self.data["armour"] is not None:
            for part in self.data["armour"]:
                self.protection += part["protection"]

    def buff(self) -> None:
        if self.data["potion"] is not None:
            for effect in self.data["potion"]["effect"]:
                if effect == "hp":
                    self.hp += self.data["potion"]["effect"]["hp"]

                if effect == "power":
                    self.power += self.data["potion"]["effect"]["power"]

                if effect == "protection":
                    self.protection += (
                        self.data["potion"]["effect"]["protection"]
                    )

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
