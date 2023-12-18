from __future__ import annotations


class Knights:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def preparation(self) -> None:
        for armour in self.armour:
            self.protection += armour.get("protection")

        if self.power:
            self.power += self.weapon.get("power")

        if self.potion:
            for key in self.potion.get("effect"):
                setattr(
                    self, key,
                    getattr(self, key) + self.potion.get("effect")[key])
        #     if "power" in self.potion.get("effect"):
        #         self.power += self.potion["effect"]["power"]
        #     if "protection" in self.potion.get("effect"):
        #         self.protection += self.potion["effect"]["protection"]
        #     if "hp" in self.potion.get("effect"):
        #         self.hp += self.potion["effect"]["hp"]

    def fight(self, other: Knights) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
